#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import time
import subprocess
import traceback


class ActivityCollector(object):
    """采集当前接入的设备中activity信息"""

    def get_current_activity_string(self):
        """
        获取当前的activity值
        :return:
        """
        output = None
        try:
            output = ""
            cmd = "adb shell dumpsys window windows | grep mCurrentFocus"
            status, output = subprocess.getstatusoutput(cmd)
            output_list = output.split(" ")
            if output_list is not None and len(output_list) > 0:
                output = output_list[len(output_list) - 1]
                output = output.replace("}", "")
            else:
                cmd = "adb shell dumpsys window windows | grep mCurrentFocus | awk '{print $3}' | sed 's/\}//g'"
                status, output = subprocess.getstatusoutput(cmd)
            if "PopupWindow" in output:
                output = "PopupWindow"
        except Exception as e:
            print("in get_current_activity_string exception")
            print(traceback.format_exc())
        finally:
            if output is not None:
                return output
            else:
                return output

    def read_store_activity_strings(self):
        """
        将文件中存储的activity获取，读取
        :return:
        """
        self.default_activity_strings = []
        store_file_path = "%s/stored_activity_strings.txt" % os.path.abspath(".")
        if os.path.exists(store_file_path):
            with open(store_file_path, "r") as store_file:
                content = store_file.read()
                if content is not None:
                    content_list = json.loads(content)
                    self.default_activity_strings = content_list

    def write_store_activity_strings(self):
        """
        将内存中的数据写入
        :return:
        """
        store_file_path = "%s/stored_activity_strings.txt" % os.path.abspath(".")
        with open(store_file_path, "w") as store_file:
            if self.default_activity_strings is not None:
                self.default_activity_strings = list(set(self.default_activity_strings))
                store_file.write(json.dumps(self.default_activity_strings))


if __name__ == '__main__':
    activity_collector = ActivityCollector()
    activity_collector.read_store_activity_strings()
    for i in range(100000):
        current_activity = activity_collector.get_current_activity_string()
        print(current_activity)
        activity_collector.default_activity_strings.append(current_activity)
        if i % 5:
            activity_collector.write_store_activity_strings()
        time.sleep(2)
