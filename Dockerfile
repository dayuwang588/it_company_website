
# 基础镜像：Python 3.10 精简版，适配 Django 4.2
FROM python:3.10-slim

# 设置容器内工作目录（所有操作都在 /app 下）
WORKDIR /app

# Python 环境配置：禁止生成 .pyc 文件，关闭输出缓冲
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 安装系统依赖（解决 Pillow 图片处理、编译依赖）
RUN apt-get update && apt-get install -y \
    gcc \
    libjpeg-dev \
    libpng-dev \
    netcat-traditional \
    && rm -rf /var/lib/apt/lists/*

# 先复制依赖文件，利用 Docker 缓存（依赖没改就不重新安装）
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 复制本地项目所有代码到容器的 /app 目录
COPY . /app/

# 创建静态/媒体/日志目录，设置权限（避免读写权限错误）
RUN mkdir -p /app/static /app/media /app/logs \
    && chmod -R 755 /app/static /app/media /app/logs

# 声明容器监听的端口（仅文档作用，实际映射在 docker-compose 中）
EXPOSE 8000

# 容器启动命令：用 Gunicorn 启动 Django（生产环境替代 runserver）
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "it_company.wsgi:application"]