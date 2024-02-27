<!-- TOC -->

- [Animals\_AI\_detection](#animals_ai_detection)
- [1 产品构建](#1-产品构建)
  - [1.1 前端](#11-前端)
  - [1.2后端](#12后端)
  - [1.3 数据集](#13-数据集)
- [2 项目流程](#2-项目流程)
  - [2.1 确定产品](#21-确定产品)
  - [2.2 产品功能](#22-产品功能)
- [DDL](#ddl)
  - [week1：](#week1)
    - [周一晚上前：团队创建报告发邮箱](#周一晚上前团队创建报告发邮箱)
    - [周二中午前：产品代办列表](#周二中午前产品代办列表)
    - [周二下午：团队会议](#周二下午团队会议)
  - [week2：](#week2)
  - [week3：](#week3)

<!-- /TOC -->

# Animals_AI_detection

题目：野趣识别---野生动物物种识别

队名：对对队

# 1 产品构建

【金山文档】 团队创建报告(模板)
https://kdocs.cn/l/ciVBb0IdVrRg

【金山文档】 产品待办列表（总需求）
https://kdocs.cn/l/cmGLx2qCiyne

【金山文档】 Spint待办列表
https://kdocs.cn/l/ck3DnTmOwYYd

## 1.1 前端


- Vue、Django

## 1.2后端

- Django

## 1.3 数据集

|数据集|地址|
|---|---|
|国家一级保护动物一级一二三等数据集|https://aistudio.baidu.com/datasetdetail/127411|



# 2 项目流程



## 2.1 确定产品

1. 确定用户：
2. 平台样式：
3. 产品架构：



## 2.2 产品功能

1. 草图模式

2. 原型创建

- 工具：墨刀


# DDL

##  week1：
###  周一晚上前：团队创建报告发邮箱
- sheng_13@163.com 和 lishaojing@easthome.com

###  周二中午前：产品代办列表

一、项目整体需求分析和范围确认（今天2/26）
1. 确认做什么样的产品:
   1. 给什么人用---确认客户
   2. 怎么用: Web系统;手机APP，微信小程序
   3. 产品架构:三层
2. 构思产品的功能范围---原型创建设计每个页面需要包括的功能
   1. 草图模式---团队讨论，设计页面功能设计: 结合业务--需求分析-调研调研方式:同类产品;用户访谈
   2. 使用工具创建原型 (墨刀)
所有成员对最终产品的功能达成一致用户对最终产品功能达成一致

二、创建产品代表列表（明天2/27中午之前）
主要的内容：
1. 用户故事:站在用户的角度，去描述一个功能点的作用
格式: 作为(用户角色)，我可以(功能点)，以便 (作用)作为一个还没有使用该程序的摊主，我想要在本程序中注册为用户，以便我使用这个程序管理我的摆摊的财务
2. 验收条件: 站在用户的角度，使用功能的正确流程
   1. 未注册的用户身份打开程序;系统监测到该用户为注册，则自动打开注册页面
   2. 用户输入正确的用户名和两次一致的密码，并且提交，系统提示新用户注册成功并跳转到登录页面。
   3. 当输入两次不一致密码时，系统提示两次密码不一致，注册失败
   4. 当输入一个已经存在的用户名并提交，系统提示该用户已经存在，注册失败
   
三、定义需求优先级

###  周二下午：团队会议
Scrum流程中，Scrum框架，每个迭代周期称为Sprint。

前期：确认项目范围、创建产品待办列表

进入Sprint周期，每个周期固定时长。

每个Sprint周期的任务：
1. 在Sprint开始之前的半天---下一个Sprint计划会议，全体成员参加
   1. 定义**本Sprint可用时长**，人时为单位
      - 团队人数(6人) * 每日有效时长(5h) * sprint天数(5天)
      - 较好情况：150人时
   2. 按优先级对**产品待办列表**中的用户故事排序
   3. 按优先级依次对多个**用户故事**进行分解：完成一个用户故事，需要团队做哪些步骤：每个步骤分为一个任务
      - **任务**1：**设计**一个xxx页面
        - 细节：该页面的目的是，让xxx；
        - 估算时长：2人时
      - 任务2：**实现**xxx页面的创建
        - 细节：技术特点
        - 估算时长：1人时
      - 任务3：**学习**xxx
        - 细节：学习xxx
        - 估算时长：3人时
      - 任务4：设计和实现xxx数据模型
        - 细节：设计和创建一个数据模型，用来记录每个销售记录。销售记录包括：商品名称，单价，数量，交易时间。
        - 估算时长：3小时
      - 任务5：设计和实现后端销售记录创建功能
        - 细节：在云端创建一个云函数，处理前端提交的销售数据，存储到数据库中。
        - 注：实际建议设计与实现分开
        - 时间：6小时
      - 任务6：设计和实现销售记录的列表显示
        - 细节：前端创建一个销售记录页面，可以分页展示所有销售记录。销售记录包括：商品名、数量、售价、交易
        - 时间：6小时
      - 任务7：设计和实现销售详情查看 6h
      - 任务8：**测试**销售记录功能 6h
      - 任务9：**统计**该用户故事的故事点 3h
   4. 统计该用户故事的故事点（总时长25）
      总工时 - 上个用户故事的时长 如 120-25 = 剩余95人时
   5. 提取下一个优先级高的用户故事，继续分解任务……（循环）
   6. 填写**Spint待办列表**，右侧三行分别为天数、理想工作量（剩余总人时）、实际工作量，填写后对应“燃尽图”。
      - 注：excel是本地表格，平台中有该部分内容。
   7. **任务分配**：
      - 待完成任务、已完成任务、无法完成的任务(Bug)。
        - 注：bug要在下个sprint最先讨论
      - 对应成员：昨天做了什么、今天打算做什么、遇到什么障碍。

总结：需要填写产品待办列表（总需求）和Spint待办列表。

##  week2：
- 

##  week3：
- 




