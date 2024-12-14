# 小说结局工厂

## 简介

小说结局工厂是一个小说结局生成器，可以生成小说结局。

## 功能

- 小说结局生成
通过调用dify工作流，生成小说结局。
- 小说结局编辑
- 小说结局分享

## 技术栈

- 前端：Bootstrap
- 后端：Python、FastAPI
- 数据库：MySQL

## 项目结构

- 前端：`/frontend`
- 后端：`/backend`

## 快速开始

### 环境要求

- Python 3.8+
- MySQL 5.7+
- 有效的 Dify API Key

### 后端服务启动

1. 安装依赖
```bash
cd backend
pip install -r requirements.txt
```

2. 配置环境变量
创建 `.env` 文件：
```bash
DATABASE_URL=mysql+aiomysql://root:password@localhost:3306/novel_ending
SECRET_KEY=your-secret-key
DIFY_API_KEY=your-dify-api-key
DIFY_API_URL=https://api.dify.ai/v1
```

3. 初始化数据库
```bash
python scripts/init_db.py
```

4. 启动服务
```bash
python -m uvicorn main:app --host 0.0.0.0 --port 7001
```

### API 使用示例

1. 创建用户
```bash
curl -X POST "http://localhost:7001/api/users/" \
     -H "Content-Type: application/json" \
     -d '{
         "username": "testuser",
         "email": "test@example.com",
         "password": "password123"
     }'
```

2. 获取访问令牌
```bash
curl -X POST "http://localhost:7001/api/auth/token" \
     -d "username=testuser&password=password123" \
     -H "Content-Type: application/x-www-form-urlencoded"
```

3. 生成小说结局
```bash
curl -X POST "http://localhost:7001/api/endings/" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{
         "work": "勇者的选择",
         "query": "请为一个勇者打败恶龙的故事写一个令人意外的结局"
     }'
```

### API 文档

启动服务后访问：
- Swagger UI: http://localhost:7001/docs
- ReDoc: http://localhost:7001/redoc

## 开发指南

### 数据库模型

#### Ending (小说结局)
- work: 作品名
- query: 生成提示
- content: 生成的结局内容
- user_id: 创建用户ID
- created_at: 创建时间
- updated_at: 更新时间

#### User (用户)
- username: 用户名
- email: 邮箱
- hashed_password: 加密后的密码
- created_at: 创建时间
- updated_at: 更新时间

### 目录结构
```
backend/
├── api/              # API路由
│   └── v1/          # API版本1
├── core/            # 核心配置
├── models/          # 数据库模型
├── schemas/         # Pydantic模型
├── services/        # 业务逻辑
├── scripts/         # 脚本工具
├── main.py         # 应用入口
├── requirements.txt # 依赖清单
└── .env            # 环境变量
```

