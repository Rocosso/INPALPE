<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>609</width>
    <height>573</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(0, 160, 227);
</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="Aceptar">
    <property name="geometry">
     <rect>
      <x>510</x>
      <y>220</y>
      <width>81</width>
      <height>251</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(223, 226, 226);</string>
    </property>
    <property name="text">
     <string>Iniciar</string>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>120</y>
      <width>211</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>Producto (nombre):</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
    </property>
    <property name="buddy">
     <cstring>Text_Nombre</cstring>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>190</y>
      <width>211</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>fecha de vencimiento:</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>300</y>
      <width>211</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>fecha de cosecha:</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="label_5">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>410</y>
      <width>211</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>Cantidad:</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
    </property>
    <property name="buddy">
     <cstring>Text_Cantidad</cstring>
    </property>
   </widget>
   <widget class="QGroupBox" name="groupBox">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>170</y>
      <width>151</width>
      <height>301</height>
     </rect>
    </property>
    <property name="toolTip">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p align=&quot;center&quot;&gt;&lt;img src=&quot;:/LOGOS/BMP&quot;/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
    <property name="title">
     <string>Seleccione una opción</string>
    </property>
    <widget class="QPushButton" name="Agregar">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>20</y>
       <width>111</width>
       <height>21</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">background-color: rgb(200, 200, 255);</string>
     </property>
     <property name="text">
      <string>Agregar</string>
     </property>
    </widget>
    <widget class="QPushButton" name="Actualizar">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>50</y>
       <width>111</width>
       <height>21</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">background-color: rgb(200, 200, 255);</string>
     </property>
     <property name="text">
      <string>Actualizar</string>
     </property>
    </widget>
    <widget class="QPushButton" name="Eliminar">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>80</y>
       <width>111</width>
       <height>21</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">background-color: rgb(200, 200, 255);</string>
     </property>
     <property name="text">
      <string>Eliminar</string>
     </property>
    </widget>
    <widget class="QPushButton" name="Mostrar_Lista">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>110</y>
       <width>111</width>
       <height>21</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">background-color: rgb(200, 200, 255);</string>
     </property>
     <property name="text">
      <string>Mostrar lista</string>
     </property>
    </widget>
    <widget class="QPushButton" name="Buscar_elemento">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>140</y>
       <width>111</width>
       <height>21</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">background-color: rgb(0, 120, 255);
background-color: rgb(200, 200, 255);</string>
     </property>
     <property name="text">
      <string>Buscar</string>
     </property>
    </widget>
    <widget class="QPushButton" name="Ordenar">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>170</y>
       <width>111</width>
       <height>21</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">background-color: rgb(200, 200, 255);</string>
     </property>
     <property name="text">
      <string>Ordenar</string>
     </property>
    </widget>
    <widget class="QPushButton" name="Almacenar">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>200</y>
       <width>111</width>
       <height>21</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">background-color: rgb(200, 200, 255);</string>
     </property>
     <property name="text">
      <string>Almacenar</string>
     </property>
    </widget>
    <widget class="QPushButton" name="Salir">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>230</y>
       <width>111</width>
       <height>21</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">background-color: rgb(200, 200, 255);</string>
     </property>
     <property name="text">
      <string>Salir</string>
     </property>
    </widget>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>400</x>
      <y>10</y>
      <width>211</width>
      <height>21</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>14</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Activo:</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="Etiqueta">
    <property name="geometry">
     <rect>
      <x>270</x>
      <y>30</y>
      <width>331</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Reem Kufi</family>
      <pointsize>20</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: rgb(255, 255, 255);</string>
    </property>
    <property name="text">
     <string>Agregar</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
    </property>
   </widget>
   <widget class="QTextEdit" name="Text_Nombre">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>140</y>
      <width>361</width>
      <height>41</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);</string>
    </property>
   </widget>
   <widget class="QTextEdit" name="Text_FV_Anio">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>240</y>
      <width>91</width>
      <height>41</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);</string>
    </property>
   </widget>
   <widget class="QTextEdit" name="Text_FV_mes">
    <property name="geometry">
     <rect>
      <x>300</x>
      <y>240</y>
      <width>91</width>
      <height>41</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);</string>
    </property>
   </widget>
   <widget class="QTextEdit" name="Text_FV_dia">
    <property name="geometry">
     <rect>
      <x>400</x>
      <y>240</y>
      <width>91</width>
      <height>41</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);</string>
    </property>
   </widget>
   <widget class="QTextEdit" name="Text_FC_mes">
    <property name="geometry">
     <rect>
      <x>300</x>
      <y>340</y>
      <width>91</width>
      <height>41</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);</string>
    </property>
   </widget>
   <widget class="QTextEdit" name="Text_FC_dia">
    <property name="geometry">
     <rect>
      <x>400</x>
      <y>340</y>
      <width>91</width>
      <height>41</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);</string>
    </property>
   </widget>
   <widget class="QTextEdit" name="Text_FC_anio">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>340</y>
      <width>91</width>
      <height>41</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);</string>
    </property>
   </widget>
   <widget class="QTextEdit" name="Text_Cantidad">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>430</y>
      <width>291</width>
      <height>41</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_7">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>320</y>
      <width>31</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>Año:</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
    </property>
    <property name="buddy">
     <cstring>Text_FC_anio</cstring>
    </property>
   </widget>
   <widget class="QLabel" name="label_8">
    <property name="geometry">
     <rect>
      <x>290</x>
      <y>320</y>
      <width>31</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>Mes:</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
    </property>
    <property name="buddy">
     <cstring>Text_FC_mes</cstring>
    </property>
   </widget>
   <widget class="QLabel" name="label_9">
    <property name="geometry">
     <rect>
      <x>390</x>
      <y>320</y>
      <width>31</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>Dia:</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
    </property>
    <property name="buddy">
     <cstring>Text_FC_dia</cstring>
    </property>
   </widget>
   <widget class="QLabel" name="label_10">
    <property name="geometry">
     <rect>
      <x>390</x>
      <y>220</y>
      <width>31</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>Dia:</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
    </property>
    <property name="buddy">
     <cstring>Text_FV_dia</cstring>
    </property>
   </widget>
   <widget class="QLabel" name="label_11">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>220</y>
      <width>31</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>Año:</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
    </property>
    <property name="buddy">
     <cstring>Text_FV_Anio</cstring>
    </property>
   </widget>
   <widget class="QLabel" name="label_12">
    <property name="geometry">
     <rect>
      <x>290</x>
      <y>220</y>
      <width>31</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>Mes:</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
    </property>
    <property name="buddy">
     <cstring>Text_FV_mes</cstring>
    </property>
   </widget>
   <widget class="QLabel" name="label_6">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>10</y>
      <width>241</width>
      <height>101</height>
     </rect>
    </property>
    <property name="whatsThis">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;img src=&quot;:/Logo/logoBMP&quot;/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
    <property name="autoFillBackground">
     <bool>false</bool>
    </property>
    <property name="styleSheet">
     <string notr="true">image: url(:/LOGOS/BMP);</string>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="pixmap">
     <pixmap resource="ResoursesGUI.qrc">:/Logo/Logo</pixmap>
    </property>
    <property name="scaledContents">
     <bool>true</bool>
    </property>
    <property name="wordWrap">
     <bool>true</bool>
    </property>
   </widget>
   <widget class="QLabel" name="label_13">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>530</y>
      <width>431</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>Desarrollado por Grupo3 Inpalpe para Estructuras de datos 2020-2</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
    </property>
    <property name="buddy">
     <cstring>Text_Cantidad</cstring>
    </property>
   </widget>
   <zorder>Aceptar</zorder>
   <zorder>label</zorder>
   <zorder>label_3</zorder>
   <zorder>label_4</zorder>
   <zorder>label_5</zorder>
   <zorder>groupBox</zorder>
   <zorder>label_2</zorder>
   <zorder>Etiqueta</zorder>
   <zorder>Text_Nombre</zorder>
   <zorder>Text_FV_Anio</zorder>
   <zorder>Text_FV_mes</zorder>
   <zorder>Text_FV_dia</zorder>
   <zorder>Text_FC_mes</zorder>
   <zorder>Text_FC_dia</zorder>
   <zorder>Text_FC_anio</zorder>
   <zorder>Text_Cantidad</zorder>
   <zorder>label_7</zorder>
   <zorder>label_8</zorder>
   <zorder>label_9</zorder>
   <zorder>label_10</zorder>
   <zorder>label_11</zorder>
   <zorder>label_12</zorder>
   <zorder>label_13</zorder>
   <zorder>label_6</zorder>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <tabstops>
  <tabstop>Agregar</tabstop>
  <tabstop>Actualizar</tabstop>
  <tabstop>Eliminar</tabstop>
  <tabstop>Mostrar_Lista</tabstop>
  <tabstop>Buscar_elemento</tabstop>
  <tabstop>Ordenar</tabstop>
  <tabstop>Almacenar</tabstop>
  <tabstop>Text_Nombre</tabstop>
  <tabstop>Text_FV_Anio</tabstop>
  <tabstop>Text_FV_mes</tabstop>
  <tabstop>Text_FV_dia</tabstop>
  <tabstop>Text_FC_anio</tabstop>
  <tabstop>Text_FC_mes</tabstop>
  <tabstop>Text_FC_dia</tabstop>
  <tabstop>Text_Cantidad</tabstop>
  <tabstop>Aceptar</tabstop>
  <tabstop>Salir</tabstop>
 </tabstops>
 <resources>
  <include location="ResoursesGUI.qrc"/>
  <include location="Imagenes.qrc"/>
 </resources>
 <connections/>
</ui>
