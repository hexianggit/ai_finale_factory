from typing import Optional
import httpx
from fastapi import HTTPException

from core.config import settings

async def generate_ending(prompt: str) -> Optional[str]:
    """调用 Dify Workflow API 生成小说结局"""
    headers = {
        "Authorization": f"Bearer {settings.DIFY_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "inputs": {
            "query": prompt,  # 主题/query字段
            "work": "小说结局生成"  # 作品名
        },
        "response_mode": "blocking",  # 使用阻塞模式，等待完整结果
        "user": "novel-ending-generator"  # 用于标识API调用来源
    }
    
    print(headers)
    print(payload)
    print(settings.DIFY_API_URL)
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{settings.DIFY_API_URL}/workflows/run",
                headers=headers,
                json=payload,
                timeout=60.0  # 增加超时时间到60秒
            )
            response.raise_for_status()
            result = response.json()
            
            # 检查工作流执行状态
            if result["data"]["status"] != "succeeded":
                raise HTTPException(
                    status_code=500,
                    detail=f"Workflow execution failed: {result['data'].get('error', 'Unknown error')}"
                )
            
            # 从输出中获取生成的结局文本
            return result["data"]["outputs"].get("text", "")
            
    except httpx.HTTPError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error calling Dify API: {str(e)}"
        ) 