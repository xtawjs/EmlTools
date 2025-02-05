# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 14:41:31 2024

@author: user
"""

import os
import glob
import email
import shutil
from email import policy
from email.parser import BytesParser

# 指定存储附件的文件夹
attachments_folder = 'attachments'
if not os.path.exists(attachments_folder):
    os.makedirs(attachments_folder)

# 遍历当前文件夹下的所有 .eml 文件
for eml_file in glob.glob('*.eml'):
    try:
        with open(eml_file, 'rb') as file:
            # 使用 BytesParser 以正确处理可能的二进制附件
            msg = BytesParser(policy=policy.default).parse(file)

            # 确保目录存在，如果不存在则创建
            folder_path = os.path.join(attachments_folder, eml_file)
            os.makedirs(folder_path, exist_ok=True)  # exist_ok=True 表示如果目录已存在不会抛出错误
            # 复制 eml_file 到 folder_path
            dst_eml_path = os.path.join(folder_path, eml_file)  # 目标路径
            shutil.copy(eml_file, dst_eml_path)

            # 遍历邮件的所有部分，查找附件
            for part in msg.walk():
                # 如果部分是附件，它将有一个“Content-Disposition”头部或特定的 Content-Type
                content_disposition = part.get_content_disposition()
                content_type = part.get_content_type()
                filename = part.get_filename()

                # 判断是否为附件
                is_attachment = (content_disposition == 'attachment' or
                                 content_type.startswith('application/') or
                                 content_type.startswith('image/') or
                                 content_type.startswith('audio/') or
                                 content_type.startswith('video/'))

                if is_attachment and filename:
                    # 处理文件名中的非 ASCII 字符
                    filename = email.header.decode_header(filename)[0][0]
                    if isinstance(filename, bytes):
                        filename = filename.decode('utf-8', errors='replace')

                    # 确保文件名唯一，避免覆盖
                    filepath = os.path.join(attachments_folder, eml_file, filename)
                    counter = 1
                    while os.path.exists(filepath):
                        name, ext = os.path.splitext(filename)
                        filepath = os.path.join(attachments_folder, f"{name}_{counter}{ext}")
                        counter += 1

                    # 保存附件
                    with open(filepath, 'wb') as fp:
                        fp.write(part.get_payload(decode=True))
                    print(f"Extracted: {filepath}")
    except Exception as e:
        print(f"Error processing file {eml_file}: {e}")