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

.. code-block:: html
   :caption: HTML 模板

   <!doctype html>
   <html>
        <head>
             <link rel="stylesheet" href="style.css">
             <title> </title>
             <style> </style>
        </head>
        <body>
             <h1> </h1> <!-- 标题共 6 级 h1 - h6 -->
             <p> </p>
             <br>
             <em> </em>
             <strong> </strong>
             <img>
             <a> </a>
             <button> </button>
        </body>
   </html>


.. code-block:: css
   :caption: CSS 模板

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
   border-radius: 30px 30px 30px 30px; /* in clockwise order: top-left top-right bottom-right bottom-left */
   padding: 50px;  /* generates space between content and border of an element. C-P-B-M */
   padding: 20px 0 20px 0; /* in clockwise order: top-right-bottom-left */
   padding-left: 200px;
   padding-right:
   padding-top:
   padding-bottom:
   text-align: center;
   margin: ;     /* generates space around an element, outside of border */
   margin-top: 20px;
   }

:numref:`html_sample` 的来源网址是 `Codecademy <https://www.codecademy.com/courses/learn-html/lessons/intro-to-html/exercises/review-html-structure>`_

.. code-block:: html
    :caption: html 简短示例
    :name: html_sample

        <body>
          <h1>The Brown Bear</h1>
          <div id="introduction">
            <h2>About Brown Bears</h2>
            <p>The brown bear (<em>Ursus arctos</em>) is native to parts of northern Eurasia and North America. Its conservation status is currently <strong>Least Concern</strong>.<br /><br /> There are many subspecies within the brown bear species, including the Atlas bear and the Himalayan brown bear.</p>
            <h3>Species</h3>
            <ul>
              <li>Arctos</li>
              <li>Collarus</li>
              <li>Horribilis</li>
              <li>Nelsoni (extinct)</li>
            </ul>
            <h3>Features</h3>
            <p>Brown bears are not always completely brown. Some can be reddish or yellowish. They have very large, curved claws and huge paws. Male brown bears are often 30% larger than female brown bears. They can range from 5 feet to 9 feet from head to toe.</p>
          </div>
          <div id="habitat">
            <h2>Habitat</h2>
            <h3>Countries with Large Brown Bear Populations</h3>
            <ol>
              <li>Russia</li>
              <li>United States</li>
              <li>Canada</li>
            </ol>
            <h3>Countries with Small Brown Bear Populations</h3>
            <p>Some countries with smaller brown bear populations include Armenia, Belarus, Bulgaria, China, Finland, France, Greece, India, Japan, Nepal, Poland, Romania, Slovenia, Turkmenistan, and Uzbekistan.</p>
          </div>
          <div id="media">
            <h2>Media</h2>
            <img src="https://content.codecademy.com/courses/web-101/web101-image_brownbear.jpg" alt="A Brown Bear"/>
            <video src="https://content.codecademy.com/courses/freelance-1/unit-1/lesson-2/htmlcss1-vid_brown-bear.mp4" width="320" height="240" controls>
            Video not supported
            </video>
          </div>
        </body>
    

.. figure:: media/html_1.png
    :align: center

    HTML+CSS+JavaScript
