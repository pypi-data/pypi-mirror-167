#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import shutil
import pathlib
import os
import requests
import functools
import tqdm
import logging
import time
import socket
import paramiko
import zipfile
from paramiko.py3compat import u
from pprint import pformat
from pyocs import pyocs_software
from pyocs.pyocs_demand import PyocsDemand

class Yadiredo:
    API_ENDPOINT = 'https://cloud-api.yandex.net/v1/disk/public/resources/?public_key={}&path=/{}&offset={}'
    _logger = logging.getLogger(__name__)
    newlink = None
    url = None
    download_root_dir = os.environ['HOME'] + '/yandex_software/'

    def __init__(self, url):
        self._logger.setLevel(level=logging.INFO)  # 控制打印级别
        self.url = url
        self.newlink = self.is_yandex_newlink(self.url)

    def download_file(self, target_path, url):
        # self._logger.info(url)
        r = requests.get(url, stream=True, allow_redirects=True)
        if r.status_code != 200:
            r.raise_for_status()  # Will only raise for 4xx codes, so...
            raise RuntimeError("请求网站时出现错误!")
        file_size = int(r.headers.get('Content-Length', 0))

        path = pathlib.Path(target_path).expanduser().resolve()
        path.parent.mkdir(parents=True, exist_ok=True)
        desc = "(Unknown total file size)" if file_size == 0 else ""
        r.raw.read = functools.partial(r.raw.read, decode_content=True)  # Decompress if needed
        with tqdm.tqdm.wrapattr(r.raw, "read", total=file_size, desc=desc) as r_raw:
            with path.open("wb") as f:
                shutil.copyfileobj(r_raw, f)


    def try_as_file(self, j, current_path):
        if 'file' in j:
            file_save_path = os.path.join(current_path, j['name'])
            self._logger.info(f' processing, file save path: ./{file_save_path}')
            self.download_file(file_save_path, j['file'])
            return True
        return False


    def get_burn_info_with_upload(self, ocs):
        sw = pyocs_software.PyocsSoftware()
        ddr_info_str = PyocsDemand(ocs).get_ddr_info()
        if not ddr_info_str:
            raise RuntimeError("无法获取DDR信息，请确认订单状态")

        ddr_info_dict = eval(ddr_info_str)

        burn_place_hold_nums = ddr_info_str.count('refDec')
        burn_place_hold_itemNo = ddr_info_dict['categoryDescp']
        flash_list1 = ['EMMC FLASH', 'NAND FLASH']
        flash_list2 = ['NOR FLASH']
        if 1 == burn_place_hold_nums:
            if ddr_info_dict['refDec'] is None:
                burn_place_hold_type = ''
                burn_type = sw.sw_burn_type["离线烧录"]
            else:
                burn_place_hold = '【' + ddr_info_dict['refDec'] + '】,' + ddr_info_dict['supplierNo'] + ',' + \
                                ddr_info_dict['itemNo'] + ',' + ddr_info_dict['categoryDescp'] + ',' + ddr_info_dict['capacity']
                burn_place_hold_type = ddr_info_dict['refDec']
                if burn_place_hold_itemNo in flash_list1:
                    burn_type = sw.sw_burn_type["在线烧录"]
                elif burn_place_hold_itemNo in flash_list2:
                    burn_type = sw.sw_burn_type["离线烧录"]
        elif 2 == burn_place_hold_nums:
            if ddr_info_dict['refDec'] is None or ddr_info_dict['refDec1'] is None:
                burn_place_hold_type = ''
                burn_type = sw.sw_burn_type["离线烧录"]
            else:
                categoryDescp = [ddr_info_dict['categoryDescp'], ddr_info_dict['categoryDescp1']]

                if categoryDescp.count('DDR') == 1:#刚好有一个是DDR，那就用非DDR的那个
                    if categoryDescp[0] == 'DDR':
                        burn_place_hold_type = ddr_info_dict['refDec1']
                        burn_place_hold_itemNo = ddr_info_dict['categoryDescp1']
                    else:
                        burn_place_hold_type = ddr_info_dict['refDec']
                        burn_place_hold_itemNo = ddr_info_dict['categoryDescp']
                    if burn_place_hold_itemNo in flash_list1:
                        burn_type = sw.sw_burn_type["在线烧录"]
                    elif burn_place_hold_itemNo in flash_list2:
                        burn_type = sw.sw_burn_type["离线烧录"]
                else:
                    self._logger.info("订单录入的烧录位号有两种，请手动设置，详情如下：")
                    burn_place_hold = '【' + ddr_info_dict['refDec'] + '】,' + ddr_info_dict['supplierNo'] + ',' + \
                                    ddr_info_dict['itemNo'] + ',' + ddr_info_dict['categoryDescp'] + ',' + ddr_info_dict['capacity']
                    burn_place_hold_option = ddr_info_dict['refDec']
                    burn_place_hold1 = '【' + ddr_info_dict['refDec1'] + '】,' + ddr_info_dict['supplierNo1'] + ',' + \
                                    ddr_info_dict['itemNo1'] + ',' + ddr_info_dict['categoryDescp1'] + ',' + ddr_info_dict['capacity1']
                    burn_place_hold_option1 = ddr_info_dict['refDec1']
                    burn_place_hold_str = '请输入烧录位号选项' + '(' + burn_place_hold_option + ', ' + burn_place_hold_option1 + '): '
                    burn_place_hold_type = input(burn_place_hold_str)
                    burn_place_hold_type = burn_place_hold_type.upper()
                    burn_type = input("请输入烧录类型选项(1,2)：")
        elif 3 == burn_place_hold_nums:
            if ddr_info_dict['refDec'] is None or ddr_info_dict['refDec1'] is None or ddr_info_dict['refDec2'] is None:
                burn_place_hold_type = ''
                burn_type = sw.sw_burn_type["离线烧录"]
            else:
                categoryDescp = [ddr_info_dict['categoryDescp'], ddr_info_dict['categoryDescp1'], ddr_info_dict['categoryDescp2']]

                if categoryDescp.count('DDR') == 2:#刚好有两个是DDR，那就用非DDR的那个
                    if categoryDescp[0] != 'DDR':
                        burn_place_hold_type=ddr_info_dict['refDec']
                        burn_place_hold_itemNo = ddr_info_dict['categoryDescp']
                    elif categoryDescp[1] != 'DDR':
                        burn_place_hold_type = ddr_info_dict['refDec1']
                        burn_place_hold_itemNo = ddr_info_dict['categoryDescp1']
                    else:
                        burn_place_hold_type = ddr_info_dict['refDec2']
                        burn_place_hold_itemNo = ddr_info_dict['categoryDescp2']
                    if burn_place_hold_itemNo in flash_list1:
                        burn_type = sw.sw_burn_type["在线烧录"]
                    elif burn_place_hold_itemNo in flash_list2:
                        burn_type = sw.sw_burn_type["离线烧录"]
                else:
                    self._logger.info("订单录入的烧录位号有两种，请手动设置，详情如下：")
                    burn_place_hold = '【' + ddr_info_dict['refDec'] + '】,' + ddr_info_dict['supplierNo'] + ',' + \
                                    ddr_info_dict['itemNo'] + ',' + ddr_info_dict['categoryDescp'] + ',' + ddr_info_dict['capacity']
                    burn_place_hold_option = ddr_info_dict['refDec']
                    burn_place_hold1 = '【' + ddr_info_dict['refDec1'] + '】,' + ddr_info_dict['supplierNo1'] + ',' + \
                                    ddr_info_dict['itemNo1'] + ',' + ddr_info_dict['categoryDescp1'] + ',' + ddr_info_dict['capacity1']
                    burn_place_hold_option1 = ddr_info_dict['refDec1']
                    burn_place_hold2 = '【' + ddr_info_dict['refDec2'] + '】,' + ddr_info_dict['supplierNo2'] + ',' + \
                                    ddr_info_dict['itemNo2'] + ',' + ddr_info_dict['categoryDescp2'] + ',' + ddr_info_dict['capacity2']
                    burn_place_hold_option2 = ddr_info_dict['refDec2']
                    burn_place_hold_str = '请输入烧录位号选项' + '(' + burn_place_hold_option + ', ' + burn_place_hold_option1 + burn_place_hold_option2 + '): '
                    burn_place_hold_type = input(burn_place_hold_str)
                    burn_place_hold_type = burn_place_hold_type.upper()
                    burn_type = input("请输入烧录类型选项(1,2)：")
        else:
            log.error("存储器信息异常")
        return burn_place_hold_type, burn_type


    def remove_ndays_before_create_dir(self, day):
        for dir in os.listdir(self.download_root_dir):
            temp_path = os.path.join(self.download_root_dir, dir)
            dir_create_time = os.path.getctime(temp_path)
            current_time = time.time()
            if current_time - dir_create_time > (24*60*60) * int(day):
                shutil.rmtree(temp_path)


    def init_reset_env(self,target_path, source_path):
        try:
            self.remove_ndays_before_create_dir(7)
            current_path = pathlib.Path(target_path, source_path)
            shutil.rmtree(current_path)
        except FileNotFoundError:
            pass
        current_path = os.path.join(target_path, source_path)
        current_path = os.path.join(target_path, source_path)
        pathlib.Path(current_path).mkdir(parents=True, exist_ok=True)


    def list_all_files(self, target_path):
        files = []
        fdlist = os.listdir(target_path) #列出文件夹下所有的目录与文件
        for i in range(0,len(fdlist)):
            path = os.path.join(target_path,fdlist[i])
            if os.path.isdir(path):
                files.extend(self.list_all_files(path))
            if os.path.isfile(path):
                files.append(path)
        return files


    def upload_zip_to_ocs(self, zip_path, xml_path, target_path, ocs, disable_origin_sw=True):
        self._logger.info(f'uploading {zip_path} ...')

        sw = pyocs_software.PyocsSoftware()
        demand = pyocs_software.PyocsDemand(ocs)
        task_type = demand.get_task_type()
        test_type = '100' #不用测试
        if (task_type=='虚拟软件任务' or task_type == '生产软件任务'):
            self._logger.info(f'Task type is production order.')
            test_type='5' #默认E测

        burn_place_hold_type, burn_type = self.get_burn_info_with_upload(ocs)

        ret = sw.upload_software_to_ocs(ocs_num=ocs, zip_path=zip_path, xml_path=xml_path,
                test_type=test_type, burn_place_hold=burn_place_hold_type,
                burn_type=burn_type, message="Auto upload yandex software.",disable_origin_sw=disable_origin_sw)

        return ret

    def unpack_rename_upload_yandex_software(self, target_path, source_path, ocs):
        #unpack
        self._logger.info(f'*** unpack...')
        start_time = time.time()
        for it in pathlib.Path(target_path).iterdir():
            zip_file_path = pathlib.Path(target_path).joinpath(it.name)
            if zipfile.is_zipfile(zip_file_path):
                shutil._unpack_zipfile(zip_file_path, target_path)
        end_time = time.time()
        self._logger.info("Unpack used time: {:.2f} S".format(end_time - start_time))

        #rename & repakage
        files = self.list_all_files(target_path)
        for fi in files:
            if '.xml' in fi:
                sw_xml_file = fi
                new_usb_sw_name = fi.split('/')[-1].replace('.xml', '')
            if 'sos.bin' in fi:
                usb_bin_file = fi
            if 'mboot.bin' in fi:
                mboot_file = fi
            if 'rom_emmc_boot.bin' in fi:
                rom_emmc_boot_file = fi
            if 'NativeEmmc.bin' in fi:
                native_emmc_file = fi

        self._logger.info(f'*** make usb upgrade zip package...')
        start_time = time.time()
        usb_sw_path = os.path.join(target_path, 'usb_sw')
        if os.path.exists(usb_sw_path):
            shutil.rmtree(usb_sw_path) # 如果路径存在，先删除，之后再重建，避免前一次的异常，影响到重新处理
        pathlib.Path(usb_sw_path).mkdir(parents=True, exist_ok=True)
        shutil.move(usb_bin_file, usb_sw_path)
        shutil.move(mboot_file, usb_sw_path)
        base_name = target_path + '/' + new_usb_sw_name
        zip_usb_path = shutil.make_archive(base_name, 'zip', root_dir=target_path, base_dir='usb_sw', logger=self._logger)
        end_time = time.time()
        self._logger.info("Make usb upgrade zip packge used time: {:.2f} S".format(end_time - start_time))

        #calculate checksum
        p = os.popen('CalChecksum ' + rom_emmc_boot_file + ' ' + native_emmc_file)
        checksum = p.read().strip()
        self._logger.info(f'EMMCBIN checksum: {checksum}')

        self._logger.info(f'*** make EMMCBIN  zip package...')
        start_time = time.time()
        emmc_bin_sw_path = os.path.join(target_path, 'emmc_bin_sw')
        if os.path.exists(emmc_bin_sw_path):
            shutil.rmtree(emmc_bin_sw_path) # 如果路径存在，先删除，之后再重建，避免前一次的异常，影响到重新处理
        pathlib.Path(emmc_bin_sw_path).mkdir(parents=True, exist_ok=True)
        shutil.move(rom_emmc_boot_file, emmc_bin_sw_path)
        shutil.move(native_emmc_file, emmc_bin_sw_path)
        base_name = target_path + '/EMMCBIN_' + checksum + '_' + new_usb_sw_name
        zip_emmcbin_path = shutil.make_archive(base_name, 'zip', root_dir=target_path, base_dir='emmc_bin_sw', logger=self._logger)
        end_time = time.time()
        self._logger.info("Make EMMCBIN zip package used time: {:.2f} S".format(end_time - start_time))

        xml_path = shutil.move(sw_xml_file, target_path)

        if not ocs:
            ocs = new_usb_sw_name[2:8]
            self._logger.info(f'ocs : {ocs}')

        #upload to ocs
        start_time = time.time()
        ret1 = self.upload_zip_to_ocs(zip_usb_path, xml_path, target_path, ocs)
        if ret1:
            self._logger.info(f'upload yandex usb upgrade package succeed to {ocs}')
        else:
            self._logger.warn(f'upload yandex usb upgrade package failure to {ocs}')
        end_time = time.time()
        self._logger.info("Upload usb upgrade package to ocs used time: {:.2f} S".format(end_time - start_time))

        start_time = time.time()
        ret2 = self.upload_zip_to_ocs(zip_emmcbin_path, xml_path, target_path, ocs, disable_origin_sw=False)
        if ret2:
            self._logger.info(f'upload yandex emmcbin package succeed to {ocs}')
        else:
            self._logger.warn(f'upload yandex emmcbin package failure to {ocs}')
        end_time = time.time()
        self._logger.info("Upload emmcbin package to ocs used time: {:.2f} S".format(end_time - start_time))


    def download_path(self, target_path, public_key, source_path, offset=0):
        # self._logger.info('getting "{}" at offset {}'.format(source_path, offset))
        current_path = os.path.join(target_path, source_path)
        pathlib.Path(current_path).mkdir(parents=True, exist_ok=True)
        jsn = requests.get(self.API_ENDPOINT.format(public_key, source_path, offset)).json()

        # first try to treat the actual json as a single file description
        if self.try_as_file(jsn, current_path):
            return

        # otherwise treat it as a directory
        try:
            emb = jsn['_embedded']
        except KeyError:
            log.error(pformat(jsn))
            return
        items = emb['items']
        for i in items:
            # each item can be a file...
            if self.try_as_file(i, current_path):
                continue
            # ... or a directory
            else:
                subdir_path = os.path.join(source_path, i['name'])
                self.download_path(target_path, public_key, subdir_path)

        # check if current directory has more items
        last = offset + emb['limit']
        if last < emb['total']:
            self.download_path(target_path, public_key, source_path, last)


    def is_yandex_newlink(self, url):
        prefix_oldlink = "https://disk.yandex.ru/d"
        prefix_newlink = "https://quasar.s3.yandex.net"
        if prefix_newlink in url:
            return True
        elif prefix_oldlink in url:
            return False
        else:
            raise RuntimeError("Unknown URL:" + url)


    def download_for_newlink(self, target_path, url):
        temp = target_path.split('/')
        file_save_path = target_path + '/' + temp[-1] + '.zip'
        self._logger.info(f' processing, file save path: ./{file_save_path}')
        self.download_file(file_save_path, url)


    def yandex_download_upload(self, remote=False, ocs=None):
        self.newlink = self.is_yandex_newlink(self.url)
        temp = self.url.split('/')

        temp_dir_name = None
        if self.newlink:
            temp_dir_name = temp[-1].strip('.zip')
        else :
            temp_dir_name = temp[-1]

        target_path = self.download_root_dir + temp_dir_name
        source_path = ''

        if remote:
            self.remote_ssh_server(self.url, ocs)
        else:
            self.init_reset_env(target_path, source_path)
            if self.newlink:
                self.download_for_newlink(target_path, self.url)
            else:
                self.download_path(target_path, self.url, source_path)

            self.unpack_rename_upload_yandex_software(target_path, source_path, ocs)


    def remote_ssh_server(self, url, ocs):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        hostname = '10.22.1.49'
        port = 22
        username = 'iot_common'
        pkey = paramiko.RSAKey.from_private_key_file(os.environ['HOME'] + '/.ssh/id_rsa')

        self._logger.info(f'*** Connecting... {username}@{hostname} ')
        client.connect(hostname=hostname, port=port, username=username, pkey=pkey)
        channel = client.invoke_shell()
        self._logger.info(f'*** Successfully connected!')

        if ocs != None :
            downlod_cmd = 'pyocs yandex ' + url + ' --ocs=' + ocs +' \t\n'
        else:
            downlod_cmd = 'pyocs yandex ' + url + ' \t\n'

        channel.send(downlod_cmd)
        remote_text = ''

        while True:
            time.sleep(2)
            try:
                recv_content = u(channel.recv(1024))
                print(recv_content)
                remote_text += recv_content
                if (("upload yandex usb" in remote_text) and ("upload yandex emmcbin" in remote_text)):
                    break
            except UnicodeDecodeError:
                pass

        client.close()

if __name__ == '__main__':
    d = Yadiredo('https://disk.yandex.ru/d/k_1RjGmY8rfKTA')
    d.yandex_download_upload()