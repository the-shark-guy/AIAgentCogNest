"""
滑动窗口切片策略
固定长度、有重叠的文本分割方法
"""

def sliding_window_chunking(text, window_size=512, step_size=256):
    """滑动窗口切片"""
    chunks = []
    
    # 使用step_size作为步长,从文本开头遍历到结尾
    for i in range(0, len(text), step_size):
        # 从位置i开始,截取window_size长度的文本片段
        chunk = text[i:i + window_size]
        
        # 去除首尾空白字符,如果切片不为空则添加到结果列表
        if len(chunk.strip()) > 0:
            chunks.append(chunk.strip())
    
    # 返回所有切片结果
    return chunks

def print_chunk_analysis(chunks, method_name):
    """打印切片分析结果"""
    print(f"\n{'='*60}")
    print(f"📋 {method_name}")
    print(f"{'='*60}")
    
    if not chunks:
        print("❌ 未生成任何切片")
        return
    
    total_length = sum(len(chunk) for chunk in chunks)
    avg_length = total_length / len(chunks)
    min_length = min(len(chunk) for chunk in chunks)
    max_length = max(len(chunk) for chunk in chunks)
    
    print(f"📊 统计信息:")
    print(f"   - 切片数量: {len(chunks)}")
    print(f"   - 平均长度: {avg_length:.1f} 字符")
    print(f"   - 最短长度: {min_length} 字符")
    print(f"   - 最长长度: {max_length} 字符")
    print(f"   - 长度方差: {max_length - min_length} 字符")
    
    print(f"\n📝 切片内容:")
    for i, chunk in enumerate(chunks, 1):
        print(f"   块 {i} ({len(chunk)} 字符):")
        print(f"   {chunk}")
        print()

# 测试文本
text = """
迪士尼乐园提供多种门票类型以满足不同游客需求。一日票是最基础的门票类型，可在购买时选定日期使用，价格根据季节浮动。两日票需要连续两天使用，总价比购买两天单日票优惠约9折。特定日票包含部分节庆活动时段，需注意门票标注的有效期限。

购票渠道以官方渠道为主，包括上海迪士尼官网、官方App、微信公众号及小程序。第三方平台如飞猪、携程等合作代理商也可购票，但需认准官方授权标识。所有电子票需绑定身份证件，港澳台居民可用通行证，外籍游客用护照，儿童票需提供出生证明或户口本复印件。

生日福利需在官方渠道登记，可获赠生日徽章和甜品券。半年内有效结婚证持有者可购买特别套票，含皇家宴会厅双人餐。军人优惠现役及退役军人凭证件享8折，需至少提前3天登记审批。
"""

if __name__ == "__main__":
    print("🎯 滑动窗口切片策略测试")
    print(f"📄 测试文本长度: {len(text)} 字符")
    
    # 使用滑动窗口切片
    chunks = sliding_window_chunking(text, window_size=300, step_size=150)
    print_chunk_analysis(chunks, "滑动窗口切片") 