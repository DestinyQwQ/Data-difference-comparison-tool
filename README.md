# 数据差异比对工具 (Data-difference-comparison-tool)

用于快速比对两个文本文件的内容差异，支持展示独有数据、统计信息及结果导出。

## 开发流程
 <center><img src="https://github.com/DestinyQwQ/Data-difference-comparison-tool/blob/main/%E6%95%B0%E6%8D%AE%E5%B7%AE%E5%BC%82%E6%AF%94%E5%AF%B9%20v1.0.png" alt="开发流程" width="60%"/></center>

## 功能特点
- **可视化操作**：简洁的 GUI 界面，无需命令行操作。

  <img src="https://github.com/DestinyQwQ/Data-difference-comparison-tool/blob/main/images/1.png" alt="主界面" width="60%"/>
- **核心功能**：
  - 选择两个文本文件（.txt），每一行代表一个数据对象。
 
    <img src="https://github.com/DestinyQwQ/Data-difference-comparison-tool/blob/main/images/a.png" alt="1.txt" width="40%"/>
    <img src="https://github.com/DestinyQwQ/Data-difference-comparison-tool/blob/main/images/b.png" alt="2.txt" width="40%"/>
   
  - 自动识别文件内容差异，分类展示「仅在文件1中」「仅在文件2中」的数据
  - 生成详细统计：文件总数据量、独有数据量、共有数据量、差异总量
  - 支持将比对结果导出为文本文件
  - 一键清空历史结果，方便重复比对


## 环境要求
- Python 3.6 及以上（依赖 Python 标准库，无需额外安装第三方包）


## 快速开始
1. **克隆仓库**
   ```bash
   git clone https://github.com/DestinyQwQ/Data-difference-comparison-tool.git
   cd Data-difference-comparison-tool
   ```

2. **运行程序**
   直接执行 Python 脚本：
   ```bash
   python data_comparator.py
   ```

3. **使用步骤**
   1. 点击「浏览」按钮，分别选择需要比对的 **文件1** 和 **文件2**
   2. 点击「开始比对」，等待分析差异
   3. 在「比对结果」选项卡中查看：
      - 「仅在文件1中」：文件1独有的数据
      - 「仅在文件2中」：文件2独有的数据
      - 「统计信息」：详细的数据量统计
   4. （可选）点击「保存结果」，选择目录导出差异数据；点击「清空结果」可重新比对

   <img src="https://github.com/DestinyQwQ/Data-difference-comparison-tool/blob/main/images/2.png" alt="1" width="30%"/>
   <img src="https://github.com/DestinyQwQ/Data-difference-comparison-tool/blob/main/images/3.png" alt="2" width="30%"/>
   <img src="https://github.com/DestinyQwQ/Data-difference-comparison-tool/blob/main/images/4.png" alt="3" width="35%"/>

## 开发技术栈
- 界面框架：Tkinter
- 核心算法：集合运算（差集、交集）实现数据比对
- 文件处理：Python 内置 `os` 模块、文件 IO 操作


## 注意事项
1. 目前仅支持 **文本文件** 比对，非文本文件（如Excel）会导致读取错误
2. 建议比对编码为 **UTF-8** 的文件，其他编码（如 GBK）可能出现乱码（可在 `read_file_data` 方法中修改 `encoding` 参数）


## 写在最后
欢迎提交 Issue 反馈问题，或 Fork 仓库后提交 Pull Request 优化功能！
