for i in range(1,6):
    print(i**2)



    # 웹 서버에 요청이 오면 장고로 전달된다 
    # 특정 function 을 호출하고 싶으면 그 function에 대한 주소를 지정해서 부른다. 
    # 앞 부분은 서버 나머지는 서버내의 특정 리소스를 의미 ////// 어떤 주소를 치면 그 주소에 상응하는 함수를 부르게 된다. 
    # urlresolver 는 웹 페이지의 주소를 가져와 무엇을 할지 확인해야한다.규명하는 역할
    # 요청이 들어오면 그 요청을 목록과 쭉 비교해서 일치하는 것을 찾는다. 
    # view 어떤 url 과 연결되어 있는 함수를 지칭하는 말 