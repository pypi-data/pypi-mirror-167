# 智能报告组件

## 1. 目录结构

```bash
│__ __init__.py
│__ tmp                     # 临时文件夹
│    │__ xxx.png            	# 存放生成echarts图的临时图片文件
│    │__ xxx.html           	# 存放生成echarts图的临时html文件
│
│__ template								# 模板文件夹
│    │__ demo.docx						# 模板文件(所有智能报告模板均从该模板复制后创建,避免内容显示问题!)
│    │__ table_styles.docx  	# 内置表格style预览文件
│
│__ package                 # 工具包
│    │__ __init__.py				
│    │__ base.py							# 基类
│    │__ content.py						# 正文
│    │__ paragraph.py					# 段落
│    │__ picture.py						# 图片
│    │__ table.py							# 表格
│    │__ title.py							# 标题
│	   │__ chart.py							# echart图
│
│__ utils.py								# 常用工具
│__ constants.py						# 常量
│__ config.py								# 报告样式基类
│__ report.py								# 报告处理和生成
│__ test.py									# 测试
│__ README.md								# 文档

```

## 2. 简介

### 2.1 创建和保存文件

#### 2.1.1 从空白文件创建

```python


# 文件保存路径
filename = "test.docx"
# 报告所需数据
data = dict()
report = SmartReportBase(filename=filename, data=data)
doc_obj = report.doc_obj
doc_obj.add_paragraph(text="自动化报告,从空白文件创建!")
report.generate()
```

#### 2.1.2 从模板文件创建

模板文匹配顺序, 先在`template`文件夹搜寻, 后从根目录开始搜寻.

```python
# 文件保存路径
filename = "test.docx"
# 报告所需数据
data = dict()
# 模板文件路径
template = "xxxxx.docx"
data = dict()
report = SmartReportBase(filename=filename, data=data,template=template)
doc_obj = report.doc_obj
doc_obj.add_paragraph(text="自动化报告,从空白文件创建!")
report.generate() 
```

### 2.2 文章结构

#### 2.2.1 标题

```
report = SmartReportBase(filename=filename, data=data,template=template)
doc_obj = report.doc_obj

doc_obj.add_paragraph(text="自动化报告,从空白文件创建!")
```



#### 2.2.2 副标题

#### 2.2.3 摘要

#### 2.2.4 正文内容

#### 2.2.5 一级章节

#### 2.2.6 二级章节

#### 2.2.7 三级章节

#### 2.2.8 四级章节

### 2.3 添加非文本内容

#### 2.3.1 表格

#### 2.3.2 图片

#### 2.3.3 echarts图片

## 3. 样式基类

-   `DocStylesBase`类

      作用: 为文档样式基类, 供所有样式继承, .

    -   **to_dict()**

        将样式属性值转为字典对象, 方便遍历.

    -   **\__iter__()**

        支持样式属性遍历.

    -   **\__getitem__****(item)**

        提供[attr]取值方法.

```python
class DocStylesBase(object):
    """文本样式基类"""

    def to_dict(self):
        """转字典"""
        styles = dict()
        for attr in dir(self):
            if attr.startswith('__') or callable(attr):
                continue
            value = getattr(self, attr)
            # 自定义的Enum类型,需转成实际数值
            if isinstance(value, (DocFontFamily, DocAlignment, TableLandscapeAlignment,
                                  TableVerticalAlignment, DocFontSize)):
                value = value.value
            styles[attr] = value
        return styles

    def __iter__(self):
        for attr in self.to_dict():
            yield attr

    def __getitem__(self, item):
        return self.to_dict()[item]
```

### 3.1 页面样式

#### 3.1.1 基本样式

```Python
class PageStyleBase(DocStylesBase):
    """页面样式基类"""
    page_width = 21.00  # 页面宽度
    page_height = 29.70  # 页面高度
    left_margin = 3.17  # 左边距cm
    right_margin = 3.17  # 右边距cm
    top_margin = 2.54  # 上边距cm
    bottom_margin = 2.54  # 底边距cm
    orientation = Orientation.portrait  # 纸张方向: 默认纵向portrait
```

#### 3.1.2 页眉

推荐在模板中创建.

#### 3.1.3 页脚

推荐在模板中创建.

#### 3.1.4 页码

推荐在模板中创建.

### 3.2 文本样式

#### 3.2.1 文本样式基类

```Python
class ParagraphStyleBase(DocStylesBase):
    """段落样式基类"""
    font_size = DocFontSize.SmallFour
    text_align = DocAlignment.justify
    font_weight = False
    color = '#000000'
    font_type = DocFontFamily.MSYH # 中文字体类型
    west_font_type = DocFontFamily.MSYH  # 西文字体类型
    line_indent = True
    line_spacing = None
    style = 'Normal'
    space_before = 5
    space_after = 5
    italic = False
```

#### 3.2.2 文章标题

```Python
class PaperTitleStyleBase(TitleStyleBase):
    """文章标题样式基类"""
    font_size = DocFontSize.SmallTwo
    text_align = DocAlignment.center
    font_weight = True
    level = 0  # 文章标题
    line_spacing = 1.5
    space_before = 10
```

#### 3.2.3 文章副标题

```Python
class PaperSubTitleStyleBase(TitleStyleBase):
    """文章副标题样式基类"""
    font_size = DocFontSize.SmallFour
    text_align = DocAlignment.center
    font_weight = True
    level = 0  # 文章副标题
    line_spacing = 1.5
    space_before = 10
```

#### 3.2.4 摘要

```Python
class AbstractStyleBase(ContentStyleBase):
    """摘要样式基类"""
    font_size = DocFontSize.SmallFour
    font_weight = True
    font_type = DocFontFamily.KT
    west_font_type = DocFontFamily.MSYH
    line_spacing = 1
    space_before = 10
    space_after = 30
```

#### 3.2.5 目录

非Windows环境下, 无法通过`win32api`调用Microsoft Office, 完成目录创建及刷新操作. 

故推荐在模板中创建好目录,文件生成后手动刷新.

#### 3.2.6 正文内容

```Python
class ContentStyleBase(DocStylesBase):
    """正文样式基类"""
    font_size = DocFontSize.Four
    text_align = DocAlignment.justify
    font_weight = False
    color = '#000000'
    font_type = DocFontFamily.MSYH
    west_font_type = DocFontFamily.MSYH  # 字体类型
    line_indent = True
    line_spacing = 1.5
    style = 'Normal'
    space_before = 5
    space_after = 5
    italic = False
    paragraph_underline = None
```

#### 3.2.7 一级章节标题

```Python
class FirstTitleStyleBase(TitleStyleBase):
    """段落: 一级标题样式基类"""
    font_weight = True
    level = 1  # 段落一级标题: 如"1.xxx"
    line_spacing = 1.5
    space_before = 10
```

#### 3.2.8 二级章节标题

```Python
class SecondTitleStyleBase(TitleStyleBase):
    """段落: 二级级标题样式基类"""
    font_size = DocFontSize.Four
    font_weight = True
    level = 2  # 段落二级标题, 如"1.1 xxx"
    line_spacing = 1.5
    space_before = 5
```

#### 3.2.9 三级章节标题

```Python
class ThirdTitleStyleBase(TitleStyleBase):
    """段落: 三级标题样式基类"""
    font_size = DocFontSize.SmallFour
    font_weight = True
    level = 3  # 段落三级标题, 如"1.1.1 xxx"
    line_spacing = 1.5
    space_before = 10
```

#### 3.2.10 四级章节标题

```Python
class FourthTitleStyleBase(TitleStyleBase):
    """段落: 四级标题样式基类"""
    font_size = DocFontSize.Five
    font_weight = True
    level = 4  # 段落四级标题, 如"1.1.1.1 xxx"
    line_spacing = 1.5
    space_before = 10
```

#### 3.2.11 下划线标题

```Python
class UnderlineTitleStyleBase(TitleStyleBase):
    """下划线标题(正文内容)"""
    font_size = DocFontSize.Five
    text_align = DocAlignment.justify
    color = '#042D86'
    font_weight = True
    line_indent = False
    line_spacing = 1
    level = None
    space_before = 10
    space_after = 5
    paragraph_underline = {
        "sz": 15,  # 粗细程度
        "color": "#042D86",  # 颜色
        "val": "single"  # 线条类型
    }
```

### 3.3 表格样式

```Python
class TableStyleBase(DocStylesBase):
    """表格样式基类"""
    alignment = TableLandscapeAlignment.center  # 水平对齐方式
    vertical_alignment = TableVerticalAlignment.center  # 垂直对齐方式
    font_size = DocFontSize.Five
    font_type = DocFontFamily.MSYH  # 中文字体类型
    west_font_type = DocFontFamily.MSYH  # 西文字体类型
    font_weight = False
    color = '#000000'
    italic = False
    underline = 0
    autofit = True  # 自动调整表格宽度
    background = None  # 单元格背景色
```

#### 3.3.1 表格标题

```python
class TableTitleStyleBase(TitleStyleBase):
    """表格标题样式基类"""
    font_size = DocFontSize.Five
    font_weight = True
    level = None
    line_spacing = 1.5
    space_before = 5
    space_after = 0
    underline = 0
    background = None
```

#### 3.3.2 表头

```python
class TableHeadStyleBase(TitleStyleBase):
    """表格首部样式基类"""
    font_size = DocFontSize.Five
    font_weight = True
    level = None
    line_spacing = 1.5
    space_before = 5
    space_after = 0
    background = None  # 单元格背景色
```

#### 3.3.3 表体

```python
class TableBodyStyleBase(TableStyleBase):
    """表格内容样式基类"""
    pass
```

### 3.4 图片样式

#### 3.4.1 图片标题

```python
class PicTitleStyleBase(TitleStyleBase):
    """图片标题样式基类"""
    font_size = DocFontSize.Five
    level = None
```

#### 3.4.2 图片

```python
class PicImgStyleBase(DocStylesBase):
    """图片样式基类"""
    zom_rate = 1  # 缩放率(按比例缩放): 默认为1
    alignment = DocAlignment.center
```

## 4. API

### 4.1 package

#### 4.1.1 base

#### 4.1.2 paragraph

#### 4.1.3 title

#### 4.1.4 content

#### 4.1.5 table

#### 4.1.6 picture

#### 4.1.7 chart

### 4.2 config

### 4.3 constants

### 4.4 utils

### 4.5 report

#### 4.5.1 创建报告数据类

```python
# 继承SmartReportData,自定义报告数据
class SmartReportData(SmartReportDataBase):
    """智能报告数据"""

```

-   SmartReportData类
    -   功能
        -   按照章节封装数据获取及处理过程, 供报告生成类使用;
    -   结构
        -   \__init__
            -   传入自动化报告查询数据所需参数 `sql_client`、`neo4j_client`和`es_client`连接, 分别供MySQL、Neo4j以及ES数据查询;
            -   可接收可变参数和不定长参数, 自定义传入自动化报告所需参数;
            -   私有属性`self._data`存放所有报告所需数据;
        -   charpter_xx_xx
            -   函数名称: chapter_章节等级
                -   支持1/2/3/4级标题;
                -   数字表示顺序, 不足两位必须以数字0填充前位, 方便排序, 后续会解释;
                -   例如`chapter_01`代表"1.xxx"中的正文所需数据, `chapter_01_01`表示"1.1 xxxx"中正文所需数据, 依次类推至3级和4级标题; 
            -   命名作用
                -   为方便数据封装和获取, `SmartReportDataBase`和`SmartReportBase`中相同标题的函数命名保持一致
                -   例如针对`1.1 xxx`标题对应正文生成, `SmartReportDataBase.chapter_01_01`功能为封装数据, `SmartReportBase.chapter_01_01`功能为生成文本内容;
            -   return
                -   通过装饰器`put_chapter_data`和函数名称(例如`chapter_01_01`), 将返回的数据挂载到self._data['chapter_01_01'];
                -   `SmartReportBase`类同名函数下, 直接使用`self.get_chapter_data()`获取该标题对应数据;

#### 4.5.2 创建报告生成类

```python
class SmartReport(SmartReportBase):
    """智能报告"""
```

-   `SmartReport`类
    -   功能
        -   从`SmartReportData`类获取数据, 根据设定的样式和正文内容, 生成文档;
    -   结构
        -   \__init__
            -   filename: 文件绝对路径;
            -   data: 数据;
            -   file_cover: 

### 4.6 test

## 5. FAQ

### 5.1 模板

### 5.2 样式

