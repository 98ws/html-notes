HTML
======

:W3C: World WIde Web Consortium，国际标准化组织，制定包括 HTML、CSS、XML 等在内的 web 规范和指南。

:自闭标签: Self-closing Tag，为养成良好习惯，在文字后加上“/”进行标识。例：\ ``<meta charset="utf-8"/>``\

:非自闭标签: Non-self-closing Tag，又称为开放标签，配对出现。例：\ ``<head> ... </head>``\ 


.. list-table:: HTML 语法
    :widths: 30 70
    :header-rows: 1
    :align: left

    * - 语法
      - 说明
    * - ``<!--xxx-->``
      - 注释内容（IDEA 快捷键为 ctrl + /）。

        如 ``<!doctype html>`` 为 html 文件开头的声明、注释。
    * - ``<head> ... </head>``
      - 文件头部内容，用于设置 meta、title... 等信息。
    * - ``<h1> ... </h1>``

        ``<h2> ... </h2>``

        ``<h3> ... </h3>``
      - 标题标签，分别为一级、二级、三级。
    * - ``<p> ... </p>``
      - 段落标签（IDEA 快捷键为 p + Tab）。
    * - ``<br/>``
      - 换行标签。
    * - ``<hr/>``
      - 水平线标签。
    * - ``<strong> ... </strong>``
      - 粗体文本标签。
    * - ``<em> ... </em>``
      - 斜体文本标签。
    

.. tip::

   常见的转义符号包括：

     1. \ ``&nbsp;``\ 输出为空格；

     2. \ ``&gt;``\ 输出为大于号；

     3. \ ``&lt;``\ 输出为小于号；

     4. \ ``&copy;``\ 输出为版权符号。
