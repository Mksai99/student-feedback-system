# 📝 Student Feedback Management System

An AWS-powered, cloud-native web application that enables students to submit feedback and allows faculty/admins to view and monitor that feedback securely. This project is designed with serverless architecture and integrates DevOps practices for automation and monitoring.

---

## 🚀 Project Overview

The **Student Feedback Management System** is a full-stack cloud application developed to collect, store, and display feedback from students regarding various faculty members or courses.

- Students can rate categories like Voice Quality, Behavior, Response, and Overall Rating.
- Admins can securely log in to view faculty-wise and course-wise feedback data.
- Built using **AWS serverless architecture** (Lambda, API Gateway, DynamoDB, S3).
- Implements **CI/CD pipelines** and **monitoring with CloudWatch + SNS**.

---

## 🛠️ Features

### 👨‍🎓 Student Module
- Submits feedback through an HTML form
- Rates faculty in multiple categories using star ratings
- Sends feedback data to backend via API Gateway & Lambda

### 👨‍🏫 Admin Module
- Secure login system (credentials stored in DynamoDB)
- View feedback data in a structured HTML dashboard
- Session-based access control using custom tokens

### 🔄 DevOps Integration
- CodePipeline for auto-deploying frontend (to S3) and backend (Lambda)
- CloudWatch Metrics & Dashboards to track:
  - Total feedback count
  - Average ratings
  - Faculty/course-wise breakdown
- Alerts via Amazon SNS for critical thresholds

---

## 🧱 System Architecture

```text
Student (HTML Form)
     |
     v
API Gateway (POST)
     |
     v
AWS Lambda (submitFeedback.py)
     |
     v
DynamoDB (Feedback Table)
