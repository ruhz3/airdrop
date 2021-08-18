# Retry 항목 키워드를 에러코드 별로 저장
dic = {
    # Err Code 5100
    '5100': ['Request Time'],
    # Err Code 5200
    '5200': ['!'],
    # Err Code 5300
    '5300': ['!'],
    # Err Code 5302
    '5302': ['!'],
    # Err Code 5400
    '5400': ['Database'],
    # Err Code 5500
    '5500': ['!'],
    # Err Code 5600
    '5600': ['정상적', '시스템', '회원 자산을', '수수료를', '진행중인'],
    # Err Code 5900
    '5900': ['Unknown']
}


# 에러에 대해 재시도 여부를 반환
def decide_retry(error):
    """
    Args:
        error: {'status': '<에러코드>', 'message': '<에러 내용>'}

    Returns:
        flag: 해당 에러에 대해 재시도할 지 여부를 'Y', 'N'로 반환
    """
    flag = 'N'
    error_code = error['status']
    error_msg = error['message']

    for keyword in dic[error_code]:
        if error_msg.find(keyword) == 0:
            flag = 'Y'
            break

    return flag


print("First Test for Gitlab!")
print("Second Test for Gitlab!")