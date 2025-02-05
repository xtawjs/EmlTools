import os
import csv
from email import policy
from email.parser import BytesParser

# 检索当前目录下的所有.eml文件
eml_files = [f for f in os.listdir('.') if f.endswith('.eml')]

# 创建并打开一个CSV文件用于写入
with open('emails_info.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # 写入列标题
    writer.writerow(['邮件标题', '发件人', '收件人', '抄送人', '时间', '附件名'])

    for file_name in eml_files:
        try:
            with open(file_name, 'rb') as f:
                msg = BytesParser(policy=policy.default).parse(f)

            # 提取邮件信息
            subject = msg.get('subject', '无主题')  # 邮件标题
            from_ = msg.get('from', '未知发件人')  # 发件人
            to = msg.get('to', '未知收件人')  # 收件人
            cc = msg.get('cc', '')  # 抄送人
            date = msg.get('date', '未知时间')  # 时间
            # 附件名，多个附件名用";"分隔
            attachments = ';'.join([part.get_filename() for part in msg.iter_attachments() if part.get_filename()])

            # 写入邮件信息
            writer.writerow([subject, from_, to, cc, date, attachments])
            print(f'已读取: {subject}')
        except Exception as e:
            print(f'处理文件 {file_name} 时出错: {e}')

print('CSV邮件信息表（不含邮件文本内容）已生成。')