# About
记录PyQt5的学习过程
# 控件名称熟悉
| 控件名字 | 含义 | 
| -|-|
| objectName | 控件名称 |
| geometry | 相对坐标系 |
| sizePolicy | 控件大小策略 | 
| minimumSize | 最小尺寸 |
| maxinumSize | 最大尺寸 |
| font | 字体 |
| cursor | 光标 |
| windowTitle | 窗口标题 |
| windowIcon | 窗口图标 |
| iconSize | 图标尺寸 |
| statusTip | 任务提示栏 |
| text | 控件文本 |
| shortcut | 快捷键 |
> 关于PyQt命令的详细介绍，参考<http://pyqt.sourceforge.net/Docs/PyQt5/designer.html?higglight=signal>

# 布局管理
一共有四种不同的布局管理系统：Vertical Layout, Horizontal Layout, Grid Layout, Form Layout
## QHBoxLayout
> setSizeConstraint(QLayout.SizeConstraint(int))的用法

| 参数名称 | 模式 |
| - | - |
| SetDefaultConstraint | 默认模式 |
| SetNoConstraint| 没有约束，随便改变 |
| SetMinimumSize| 有最小的约束 |
| SetFixedSize| 固定这个层的尺寸，无法改变 |
| SetMaximumSize| 有最大的约束 |
| SetMinAndMaxSize | 有最大和最小的约束 |

> setSpacing( int )调整横向之间的距离
> addWidget( QWidget )增加一个控件



## Vertical Layout

## Grid Layout
> gridlayout.addWidget(窗口控件，行位置，列位置，要合并的行数， 要合并的列数)后两个是可选项
> QtWidget.QSpacerItem(  )

# LEARN CONTNETS
## GUI窗体介绍
### QMainWindw
QMainWindow一共有四个窗口：

### 弹出式对话框

## QLabel
