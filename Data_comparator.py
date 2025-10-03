"""
author: PureY
'This project was developed with the assistance of AI.'
"""

import os
import tkinter as tk
from tkinter import filedialog,messagebox,ttk



class DataComparator:
    def __init__(self,root):
        self.root = root
        self.root.title("数据差异比对工具 v1.0")
        self.root.geometry("800x600")
        # 创建两个字符串变量，存储用户选择文件路径
        self.file1_path = tk.StringVar()
        self.file2_path = tk.StringVar()

        self.ui()

    # 创建主界面
    def ui(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky="nswe")

        # 创建文件选择区域的标签框架
        file_selector = ttk.LabelFrame(main_frame, text="文件选择", padding="10")
        file_selector.grid(row=0, column=0, columnspan=2, sticky="we", pady=(0, 10))

        # 文件1
        ttk.Label(file_selector, text="文件1：").grid(row=0, column=0, sticky="w", pady=5)
        # 创建输入框，与file1_path变量绑定
        ttk.Entry(file_selector, textvariable=self.file1_path, width=50).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(file_selector, text="浏览", command=self.browse_file1).grid(row=0, column=2, pady=5)

        # 文件2
        ttk.Label(file_selector, text="文件2：").grid(row=1, column=0, sticky="w", pady=5)
        # 创建输入框，与file2_path变量绑定
        ttk.Entry(file_selector, textvariable=self.file2_path, width=50).grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(file_selector, text="浏览", command=self.browse_file2).grid(row=1, column=2, pady=5)


        # 创建操作按钮框架
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=1, column=0, columnspan=2, pady=10)

        # 创建"开始比对"按钮
        ttk.Button(button_frame, text="开始比对", command=self.compare_data).pack(side="left", padx=5)
        # 创建"保存结果"按钮
        ttk.Button(button_frame, text="保存结果", command=self.save_results).pack(side="left", padx=5)
        # 创建"清空结果"按钮
        ttk.Button(button_frame, text="清空结果", command=self.clear_results).pack(side="left", padx=5)


        # 创建结果显示区域的标签框架
        result_frame = ttk.LabelFrame(main_frame, text="比对结果", padding="10")
        result_frame.grid(row=2, column=0, columnspan=2, sticky="nswe", pady=(10, 0))

        # 创建选项卡
        self.notebook = ttk.Notebook(result_frame)
        # 让选项卡填充整个父容器
        self.notebook.pack(fill="both", expand=True)

        # 创建"仅在文件1中"选项卡
        self.file1_only_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.file1_only_frame, text="仅在文件1中")
        self.file1_only_listbox = tk.Listbox(self.file1_only_frame)
        self.file1_only_listbox.pack(fill="both", expand=True, side="left")
        file1_scrollbar = ttk.Scrollbar(self.file1_only_frame, orient="vertical", command=self.file1_only_listbox.yview)
        file1_scrollbar.pack(side="right", fill="y")
        # 关联列表框和滚动条，当列表框内容滚动时，滚动条同步移动
        self.file1_only_listbox.config(yscrollcommand=file1_scrollbar.set)

        # 创建"仅在文件2中"选项卡
        self.file2_only_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.file2_only_frame, text="仅在文件2中")
        self.file2_only_listbox = tk.Listbox(self.file2_only_frame)
        self.file2_only_listbox.pack(fill="both", expand=True, side="left")
        file2_scrollbar = ttk.Scrollbar(self.file2_only_frame, orient="vertical", command=self.file2_only_listbox.yview)
        file2_scrollbar.pack(side="right", fill="y")
        # 关联列表框和滚动条，当列表框内容滚动时，滚动条同步移动
        self.file2_only_listbox.config(yscrollcommand=file2_scrollbar.set)

        # 创建"统计信息"选项卡
        self.stats_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.stats_frame, text="统计信息")
        # 按单词换行
        self.stats_text = tk.Text(self.stats_frame, wrap="word")
        self.stats_text.pack(fill="both", expand=True, side="left")
        # 滚动条
        stats_scrollbar = ttk.Scrollbar(self.stats_frame, orient="vertical", command=self.stats_text.yview)
        stats_scrollbar.pack(side="right", fill="y")
        self.stats_text.config(yscrollcommand=stats_scrollbar.set)

        # 实现窗口大小调整时控件自适应
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(2, weight=1)
        result_frame.columnconfigure(0, weight=1)
        result_frame.rowconfigure(0, weight=1)
        self.file1_only_frame.columnconfigure(0, weight=1)
        self.file1_only_frame.rowconfigure(0, weight=1)
        self.file2_only_frame.columnconfigure(0, weight=1)
        self.file2_only_frame.rowconfigure(0, weight=1)
        self.stats_frame.columnconfigure(0, weight=1)
        self.stats_frame.rowconfigure(0, weight=1)

    # 选择文件的方法
    def browse_file1(self):
        filename1 = filedialog.askopenfilename(
            title="请选择文件1",
            filetypes=[("Text files", "*.txt")]
        )
        if filename1:
            self.file1_path.set(filename1)

    def browse_file2(self):
        filename2 = filedialog.askopenfilename(
            title="请选择文件2",
            filetypes=[("Text files", "*.txt")]
        )
        if filename2:
            self.file2_path.set(filename2)

    # 读取文件数据的方法
    def read_file_data(self, file_path):
        try:
            # 以只读模式打开文件，指定编码为utf-8
            with open(file_path, 'r', encoding='utf-8') as file:
                # for line in file：逐行读取，将数据转换为集合
                # line.strip()：去除每行前后的空白字符(空格、换行符等)
                # if line.strip()：过滤掉空行
                # 集合(set)：自动去重，集合运算(差集、交集)
                data = set(line.strip() for line in file if line.strip())
            return data
        except Exception as e:
            # 如果读取文件出错，显示错误消息
            messagebox.showerror("错误", f"读取文件 {file_path} 失败: {str(e)}")
            return None


    # 比对数据的核心方法
    def compare_data(self):
        # 检查用户是否选择了两个文件
        if not self.file1_path.get() or not self.file2_path.get():
            messagebox.showwarning("警告", "请先选择两个文件")
            return

        # 检查文件是否真实存在
        if not os.path.exists(self.file1_path.get()):
            messagebox.showerror("错误", "文件1不存在")
            return

        if not os.path.exists(self.file2_path.get()):
            messagebox.showerror("错误", "文件2不存在")
            return

        # 读取两个文件的数据
        data1 = self.read_file_data(self.file1_path.get())
        data2 = self.read_file_data(self.file2_path.get())

        # 如果任一文件读取失败，返回
        if data1 is None or data2 is None:
            return

        # 集合运算
        only_in_file1 = data1 - data2  # 差集：仅在data1中存在的元素
        only_in_file2 = data2 - data1  # 差集：仅在data2中存在的元素
        common_data = data1 & data2    # 交集：两个集合中都存在的元素

        # 显示比对结果
        self.display_results(only_in_file1, only_in_file2, common_data, len(data1), len(data2))


    # 显示比对结果的方法
    def display_results(self, only_in_file1, only_in_file2, common_data, count1, count2):
        # 清空现有结果，0表示开始索引，tk.END表示结束索引
        self.file1_only_listbox.delete(0, tk.END)
        self.file2_only_listbox.delete(0, tk.END)
        # 文本框清除从“第一行第一列”到末尾的内容
        self.stats_text.delete(1.0, tk.END)

        # 显示仅在文件1中的数据
        # sorted()将集合转换为排序后的列表，使结果更有序
        for item in sorted(only_in_file1):
            # 向列表框添加内容，tk.END表示添加到末尾
            self.file1_only_listbox.insert(tk.END, item)

        # 显示仅在文件2中的数据
        for item in sorted(only_in_file2):
            self.file2_only_listbox.insert(tk.END, item)

        # 准备统计信息文本
        stats_info = f"""数据比对统计信息:

文件1数据量: {count1}
文件2数据量: {count2}

仅在文件1中存在的数据量: {len(only_in_file1)}
仅在文件2中存在的数据量: {len(only_in_file2)}
两个文件中都存在的数据量: {len(common_data)}

差异数据总量: {len(only_in_file1) + len(only_in_file2)}
"""
        # 向文本框插入统计信息
        self.stats_text.insert(tk.END, stats_info)

        # 显示比对完成的提示消息
        messagebox.showinfo("完成",
                            f"比对完成!\n文件1独有数据: {len(only_in_file1)} 条\n文件2独有数据: {len(only_in_file2)} 条")


    # 保存结果的方法
    def save_results(self):
        # 检查是否有结果可保存
        if self.file1_only_listbox.size() == 0 and self.file2_only_listbox.size() == 0:
            messagebox.showwarning("警告", "没有比对结果可保存")
            return
        directory = filedialog.askdirectory(title="选择保存目录")
        if not directory:
            return

        try:
            # 保存仅在文件1中的数据
            # os.path.join()用于拼接路径，确保文件保存在正确的目录下
            file1_only_path = os.path.join(directory, "仅在文件1中.txt")
            with open(file1_only_path, 'w', encoding='utf-8') as f:
                # 遍历列表框中的所有项并写入文件
                for i in range(self.file1_only_listbox.size()):
                    f.write(self.file1_only_listbox.get(i) + '\n')

            # 保存仅在文件2中的数据
            file2_only_path = os.path.join(directory, "仅在文件2中.txt")
            with open(file2_only_path, 'w', encoding='utf-8') as f:
                for i in range(self.file2_only_listbox.size()):
                    f.write(self.file2_only_listbox.get(i) + '\n')

            messagebox.showinfo("成功", f"结果已保存到:\n{directory}")
        except Exception as e:
            messagebox.showerror("错误", f"保存失败: {str(e)}")

    # 清空结果的方法
    def clear_results(self):
        """清空结果"""
        # 清空列表框和文本框内容
        self.file1_only_listbox.delete(0, tk.END)
        self.file2_only_listbox.delete(0, tk.END)
        self.stats_text.delete(1.0, tk.END)


# 程序入口
def main():
    # 创建主窗口对象，tk.Tk()是tkinter的主窗口类
    root = tk.Tk()
    # 创建DataComparator实例，将主窗口作为参数传入
    app = DataComparator(root)
    # 进入事件循环，保持窗口显示，等待用户操作
    root.mainloop()


# 如果直接运行该脚本(而不是被导入)，则执行main()函数
if __name__ == "__main__":
    main()