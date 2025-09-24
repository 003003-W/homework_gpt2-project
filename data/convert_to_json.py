import json
import os

def convert_txt_to_json(input_file, output_file):
    # 初始化数据列表
    data_list = []
    
    # 读取txt文件
    with open(input_file, 'r', encoding='utf-8') as f:
        # 按段落读取文本
        paragraphs = f.read().split('\n\n')
        
        # 处理每个段落
        for paragraph in paragraphs:
            # 清理段落（去除多余的空白字符）
            cleaned_text = ' '.join(paragraph.split()).strip()
            if cleaned_text:  # 只添加非空段落
                data_list.append({
                    "text": cleaned_text
                })
    
    # 将数据写入JSON文件
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({"data": data_list}, f, ensure_ascii=False, indent=4)

def main():
    # 设置输入输出文件路径
    input_file = 'input.txt'
    output_file = 'input.json'
    
    # 检查输入文件是否存在
    if not os.path.exists(input_file):
        print(f"错误：找不到输入文件 {input_file}")
        return
    
    try:
        convert_txt_to_json(input_file, output_file)
        print(f"转换成功！输出文件：{output_file}")
    except Exception as e:
        print(f"转换过程中出错：{str(e)}")

if __name__ == "__main__":
    main()