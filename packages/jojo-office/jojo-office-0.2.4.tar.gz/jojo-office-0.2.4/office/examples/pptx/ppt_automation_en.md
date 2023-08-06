python自动化办公 office 库：如何批量生成PPT文件
================================================

自动化办公中，经常要批量处理office文件。

本人写了一个 python office库，功能是比较强的（干货功能，全网估计找不到），
使用也很简单，分享给大家。

office库实现了对 Word, Excel, PowerPoint, pdf 文件的常用操作。
office库只支持新版的office文件（扩展名为 .pptx, .xlsx, .pptx)，
不支持office2003以前的老版本office文件（扩展名为 .doc, .xls, .ppt)。


office库安装说明：
-------------

office库仅有一个文件 office.py。该文件可以放置在当前程序目录下供当前程序使用，
或放在site-packages目录下公用。


office库依赖以下库，请安装：
python-docx, openpyxl, python-pptx, PyPDF4, pypiwin32, reportlab, playsound
```
pip install python-docx openpyxl python-pptx PyPDF4 pypiwin32 reportlab playsound -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
```

如需要导入导出DataFrame， 依赖 pandas 库，请按需要安装
```
pip install pandas -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
```



一、批量生成PowerPoint文件
----------------

自动生成PowerPoint文件的方法是：首先写一个模板PowerPoint文件，复制模板创建新文件，再填入数据。 
填入不同的数据，则产生不同的PPT文件，从而实现批量自动生成。


模板中的变量定义：

比如：模板PowerPoint文件 template.pptx,  幻灯片中的文字内容如下：
```
姓名 : {name}
年龄 : {age}
```
大括号 { } 中包含的文字叫变量, 上例中的：name, age。
在填入数据时，变量将替换为相应的值。


1, 将Excel文件作为数据源，填入PowerPoint模板文件
-------------------------

1.1 文字

datafile.xlsx 文件中，Sheet1工作表B2单元格内容是 'Peter', C2格内容是 18。

模板PowerPoint文件 template1.pptx 写成这样：
```
姓名 : {Sheet1!B2}
年龄 : {Sheet1!C2}
```
变量 {Sheet1!B2} 指明 数据来自 Excel文件的 Sheet1 工作表的 B2 单元格。
变量 {Sheet1!C2} 指明 数据来自 Excel文件的 Sheet1 工作表的 C2 单元格。

生成PPT的python程序如下：
```
import office

# 以 template1.pptx 为模板，创建 output.pptx 文件
ppt = office.open_file("output.pptx", template="template1.pptx")

# 从 datafile.xlsx 文件中取数据, 填入, 保存
ppt.fill('datafile.xlsx').save() 
```
上述程序也可以连写为一行，例如：
```
office.open_file("output.pptx", "template1.pptx").fill('datafile.xlsx').save()
```

程序运行后，生成 output.pptx 文件, 其内容如下：
```
姓名 : Peter
年龄 : 18
```


1.2 表格

可以把数据填入PPT中的表格。

datafile.xlsx 的 Sheet1工作表 B1:C4 区域有一个表格
```
name	age
Peter	18
Sam	    19
Mary	20
```


模板文件 template2.pptx 中画了一个表格 4行 X 2列，每一列的第一行写上变量(数据来源)，写成这样：




python程序如下：
```
import office


ppt = office.open_file("output.pptx", template="template2.pptx")

# 从 datafile.xlsx 文件中取数据, 填入, 保存
ppt.fill('datafile.xlsx').save() 
```
程序运行后，生成 output.pptx 文件, 其内容如下：





注：填入表格的数据行数，取决于PPT模板中表格的行数。如果Excel表格行数大于PPT表格行数，
则后面的数据不会被填入。


3.3 图表

可以把数据填入PPT中的图表，更新图表数据从而更新图表样貌。

在PowerPoint中打开模板文件 template3.pptx，画一个直方图。右键点击图表，选菜单：“编辑数据", 
则可以看到图标的数据表。初始数据表如下：


修改数据表的第一行，每一列修改为变量(数据来源)，例如：{Sheet1!B1} 表示本列的数据来自 Sheet1 的 B列。
修改后数据表如下图：



python程序如下：
```
import office

# 以 template3.pptx 为模板，创建 output.pptx 文件,  填入datafile.xlsx 文件数据, 保存
office.open_file("output.pptx", "template3.pptx").fill('datafile.xlsx').save()

```

程序运行后，生成 output.pptx 文件, 其内容如下：





在PowerPoint中打开文件 output.pptx，右键点击图表，选菜单：“编辑数据", 
则可以看到PPT图表的数据表已经被更改为Excel文件的相应数据表，如下：



事实上， office库的处理方法，就是PPT图表的数据表后, 重建图表。
注：office库的图表功能支持2D图表，不支持3D图表。因此，模板中的图标不能是3D图表类型，否则出错。


3.4  插入图片、视频、音频

如果数据是图片文件名，则可以在PPT模板中的插入该图片文件。

模板文件 template4.pptx 中画了一个文本框，填入文字，写上变量 {@Sheet1!D2}，
变量名前加上一个 ‘@’字符表明它是一个特殊变量。当它是一个图片文件名时，将插入该图片文件。
模板如图：




python程序如下：
```
import office

# 以 template4.pptx 为模板，创建 output.pptx 文件,  填入datafile.xlsx 文件数据, 保存
office.open_file("output.pptx", "template4.pptx").fill('datafile.xlsx').save()

```
注意： datafile.xlsx 文件 Sheet1!D2 的值是 "peter.jpg"， 因文件名没有指明路径，因此这个图片
要放在当前目录下。
程序运行后，生成 output.pptx 文件, 其内容如下(可见，图片被插入了)：







2, 将dictionary数据 填入PowerPoint文件
-------------------------

模板PowerPoint文件 template3.pptx 写成这样：
```
姓名 : {name}
年龄 : {age}
```
即： 有两个变量 name, age

python程序如下：
```
import office

# 数据
data = {'name': 'Peter', 'age': 18}

# 以 template3.pptx 为模板，创建 output.pptx 文件
ppt = office.open_file("output.pptx", template="template3.pptx")

# 填入数据data, 保存
ppt.fill(data).save() 
```
上述程序也可以连写为一行，例如：
```
office.open_file("output.pptx", template="template3.pptx").fill(data).save()
```

程序运行后，生成 output.pptx 文件, 其内容如下：
```
姓名 : Peter
年龄 : 18
```

如果 dictionary 是多层级的，比如：

data = { 'friend': { 'name': 'Mary', 'age': 19} }

则模板写为：
```
姓名：{friend.name}
年龄：{friend.age}
```


3, 多次填入数据
-----------------
如果数据分布在多个Excel文件或 dict 中，可以多次调用fill()填充数据，例如：
```
ppt = office.open("output.pptx", "template.pptx")

# 先填充 1.xlsx Excel数据，再填充 dict1 数据
ppt.fill('1.xlsx').fill(dict1).save()
```

4、应用示例：邀请函
----------------------
开大会，每个客户要打印一张纸的邀请函。
把客人姓名、称谓写入列表，写一个循环，生成一批PowerPoint文件, 打印它们即可。
python代码：
```
import office

persons = [
    ["张三", "先生"],
    ["李四", "女士"],
    ["王五", "总经理"],
]
filenames = []
for person in persons:
    data = {'name': person[0], 'title': person[1]}
    filename = person[0] + ".pptx"
    office.open_file(filename, "邀请函模板.pptx").fill(data).save()
    filenames.append(filename)

# 使用 print_files() 逐个打印文件
office.print_files(filenames)
```


5、应用示例：生成一张考试卷
---------------------------------
数据在 datafile.xlsx 的 '试卷'工作表中。

模板文件为 template4.pptx。

python程序如下：
```
import office

ppt = office.open_file("output.pptx", "template4.pptx")
ppt.fill('datafile.xlsx')    # 填入Excel数据
ppt.fill({'日期': '2022年'})  # 填入变量 '日期'
ppt.save()

```
程序运行后，生成 output.pptx 文件, 其内容如下：
```
Python学习试卷 初级 2022年

一、单选题：
 1、下列标识符中， 符合命名规范的是（         ）  答案： C
A、 1_a			    B、 for
C、 年龄			D、 a#b


 2、下列标识符中，不是 Python 支持的数据类型的是 （         ）  答案： A
A、 char			B、 int
C、 float			D、 str

...
```

打开模板文件template4.pptx， 看一下模板如何定义的:
```
{试卷!A1} {试卷!A2} {日期}

一、{试卷!A5}：
{@repeat {@index}、{试卷!A6}  答案： {试卷!F6}
{试卷!B6}			{试卷!C6}
{试卷!D6}			{试卷!E6}

}

二、{试卷!A12}：
{@repeat {@index}、{试卷!A13}  答案： {试卷!F13}
{试卷!B13}			{试卷!C13}
{试卷!D13}			{试卷!E13}

```
{日期} 是从 dict 数据中填入的。
其他数据均来自 '试卷'工作表

解析：

'一' 这个部分的 重复段落 分四行。

第一行是 {@index}序号、{试卷!A6}题目、{试卷!F6}答案。
{@index} 是一个特殊变量，表示重复的序号。

第二行是 {试卷!B6} 选项A 、 {试卷!C6} 选项B。

第二行是 {试卷!D6} 选项C 、 {试卷!E6} 选项D。

第四行是一个空行。表示每道题之间空一行。


