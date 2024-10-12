<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>700</width>
    <height>700</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>600</width>
    <height>700</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>700</width>
    <height>800</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 18, 255, 255), stop:1 rgba(255, 55, 55, 255));</string>
  </property>
  <widget class="QWidget" name="main">
   <property name="styleSheet">
    <string notr="true">border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));</string>
   </property>
   <widget class="QWidget" name="verticalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>701</width>
      <height>701</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <widget class="QTabWidget" name="tab_widget">
       <property name="autoFillBackground">
        <bool>false</bool>
       </property>
       <property name="styleSheet">
        <string notr="true">color:rgb(0, 170, 0);
border: 2px;
font: 10pt &quot;Microsoft YaHei UI&quot;;
</string>
       </property>
       <property name="currentIndex">
        <number>1</number>
       </property>
       <widget class="QWidget" name="picture_gen">
        <property name="styleSheet">
         <string notr="true">color:rgb(255, 170, 0);</string>
        </property>
        <attribute name="title">
         <string>Tab 1</string>
        </attribute>
        <widget class="QLabel" name="label">
         <property name="enabled">
          <bool>false</bool>
         </property>
         <property name="geometry">
          <rect>
           <x>30</x>
           <y>40</y>
           <width>621</width>
           <height>401</height>
          </rect>
         </property>
         <property name="styleSheet">
          <string notr="true">border: 2px solid ;
border-radius: 15px;
border-color: rgb(85, 25, 0);

</string>
         </property>
         <property name="text">
          <string/>
         </property>
        </widget>
        <widget class="QPushButton" name="pushButton">
         <property name="enabled">
          <bool>true</bool>
         </property>
         <property name="geometry">
          <rect>
           <x>170</x>
           <y>500</y>
           <width>331</width>
           <height>91</height>
          </rect>
         </property>
         <property name="styleSheet">
          <string notr="true">background-color:;
color: rgba(218, 141, 17, 248);
border-style: outset;
border-width: 2px;
border-radius: 10px;
border-color: beige;
min-width: 10em;
padding: 6px;
</string>
         </property>
         <property name="text">
          <string>PushButton</string>
         </property>
         <property name="checkable">
          <bool>true</bool>
         </property>
         <property name="checked">
          <bool>false</bool>
         </property>
         <property name="autoRepeat">
          <bool>false</bool>
         </property>
        </widget>
       </widget>
       <widget class="QWidget" name="audio_generation">
        <attribute name="title">
         <string>Tab 2</string>
        </attribute>
        <widget class="QPushButton" name="pushButton_2">
         <property name="geometry">
          <rect>
           <x>130</x>
           <y>80</y>
           <width>191</width>
           <height>121</height>
          </rect>
         </property>
         <property name="text">
          <string>PushButton</string>
         </property>
        </widget>
        <widget class="QPushButton" name="pushButton_3">
         <property name="geometry">
          <rect>
           <x>340</x>
           <y>80</y>
           <width>171</width>
           <height>121</height>
          </rect>
         </property>
         <property name="text">
          <string>PushButton</string>
         </property>
        </widget>
        <widget class="QPushButton" name="pushButton_4">
         <property name="geometry">
          <rect>
           <x>110</x>
           <y>240</y>
           <width>161</width>
           <height>121</height>
          </rect>
         </property>
         <property name="text">
          <string>PushButton</string>
         </property>
        </widget>
        <widget class="QPushButton" name="pushButton_5">
         <property name="geometry">
          <rect>
           <x>340</x>
           <y>230</y>
           <width>191</width>
           <height>141</height>
          </rect>
         </property>
         <property name="styleSheet">
          <string notr="true"/>
         </property>
         <property name="text">
          <string>PushButton</string>
         </property>
        </widget>
       </widget>
      </widget>
     </item>
    </layout>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
