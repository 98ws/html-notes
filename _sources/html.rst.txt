HTML
===========

<a> </a> —— opening tag and closing tag

<br> —— self-closing tag

- tag/element: make up the main structure of html files

- attribute: included in the opening tag for additional info, such as ``src|href|class|id``.

- rule: define style of certain elements, a :abbr:`CSS (Cascading Style Sheet)` file may have as many rules as possible.

- class: rules (start with "." in CSS) contained in the ``class`` attribute modify a class of elements.

- id: rule (start with "#" in CSS) contained in the ``id`` attribute modify only one element. ie, one id can only be used to one tag.

- property: defined styles included in a rule. For example, in rule ``p{color: red;}``, ``color`` is a property and its value is ``red``.

.. code:: html

   <!doctype>
   <html>
        <head>
             <link rel="stylesheet" href="style.css">
             <title> </title>
             <style> </style>
        </head>
        <body>
             <h1> </h1> /* 标题共 6 级 h1 - h6 */
             <p> </p>
             <br>
             <em> </em>
             <strong> </strong>
             <img>
             <a> </a>
             <button> </button>
        </body>
   </html>


.. code:: css

   p{
   color: red;
   background-color: blue;
   font-style: italic;
   font-weight: bold;
   font-family: Helvetica;
   font-size: 10px;
   width: 100px;
   height: 100px;
   border: solix 10px red;
   /* if an image is square (such as 100px x 100px), setting border-radius to half of the width makes the image a round circle. */
   border-radius: 50 px; 
   }






