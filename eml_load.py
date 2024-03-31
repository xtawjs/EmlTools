# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 14:41:31 2024

@author: user
"""

import os
import glob
import email
from email import policy
from email.parser import BytesParser

# 指定存储附件的文件夹
attachments_folder = 'attachments'
if not os.path.exists(attachments_folder):
    os.makedirs(attachments_folder)

# 遍历当前文件夹下的所有 .eml 文件
for eml_file in glob.glob('*.eml'):
    with open(eml_file, 'rb') as file:
        # 使用 BytesParser 以正确处理可能的二进制附件
        msg = BytesParser(policy=policy.default).parse(file)
        
        # 遍历邮件的所有部分，查找附件
        for part in msg.walk():
            # 如果部分是附件，它将有一个“Content-Disposition”头部
            if part.get_content_disposition() == 'attachment':
                filename = part.get_filename()
                # 确保文件名有效
                if filename:
                    filepath = os.path.join(attachments_folder, filename)
                    with open(filepath, 'wb') as fp:
                        fp.write(part.get_payload(decode=True))
                    print(f"Extracted: {filepath}")