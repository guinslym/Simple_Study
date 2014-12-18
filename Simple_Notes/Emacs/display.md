Emacs显示.md
这一章描述了一系列有关Emacs现在给用户显示的特性。
##刷新屏幕##
函数`redraw-frame`清除并重新显示整个给定frame的内容,这在屏幕中断时非常有用。
 -- Function: redraw-frame frame
这个函数清除并重新显示frame.
更强大的是`redraw-display`:
 -- Command: redraw-display
 这个函数清除并重新显示所有可视frames.
在Emacs中,用户输入进程占据大部分重新显示。如果你调用那些函数在输入可用时,它并不会立即重新显示，而是在所有输入都已经完成后。  
在文本终端,暂停或恢复Emacs正常也会刷新屏幕。一些终端模拟器分别记录内容,用于例如Emacs和普通序列显示的程序。如果你使用如此的1个终端,你可能想在恢复时继承重新显示。
 -- User Option: no-redraw-on-reenter
 这个变量用于控制Emacs在暂停和恢复时是否重新绘制整个屏幕。如果不是nil,代表不需要重绘制。nil代表需要重新绘制,默认是nil.