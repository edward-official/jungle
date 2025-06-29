function q1() {
  $.ajax({
    type: "GET",
    url: "http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99",
    data: {},
    success: function (response) {
      // console.log(response);
      let rows = response["RealtimeCityAir"]["row"];
      let appender = $("#names-q1");
      appender.empty();
      for(let idx=0; idx<rows.length; idx++) {
        let town = rows[idx]["MSRSTE_NM"];
        let number = rows[idx]["IDEX_MVL"];
        // console.log(town, number);
        let appendee;
        if(number<60) appendee = `<li>${town}: ${number}</li>`;
        else appendee = `<li style="color:red">${town}: ${number}</li>`;
        appender.append(appendee);
      }
    },
  });
}
/*
{RealtimeCityAir: {…}}
RealtimeCityAir
: 
RESULT
: 
{CODE: 'INFO-000', MESSAGE: '정상 처리되었습니다'}
list_total_count
: 
25
row
: 
Array(25)
0
: 
{MSRDT: '202506291400', MSRRGN_NM: '도심권', MSRSTE_NM: '중구', PM10: 15, PM25: 12, …}
1
: 
{MSRDT: '202506291400', MSRRGN_NM: '도심권', MSRSTE_NM: '종로구', PM10: 10, PM25: 10, …}
2
: 
{MSRDT: '202506291400', MSRRGN_NM: '도심권', MSRSTE_NM: '용산구', PM10: 18, PM25: 15, …}
3
: 
{MSRDT: '202506291400', MSRRGN_NM: '서북권', MSRSTE_NM: '은평구', PM10: 12, PM25: 14, …}
4
: 
{MSRDT: '202506291400', MSRRGN_NM: '서북권', MSRSTE_NM: '서대문구', PM10: 7, PM25: 4, …}
5
: 
{MSRDT: '202506291400', MSRRGN_NM: '서북권', MSRSTE_NM: '마포구', PM10: 15, PM25: 11, …}
6
: 
{MSRDT: '202506291400', MSRRGN_NM: '동북권', MSRSTE_NM: '광진구', PM10: 16, PM25: 12, …}
7
: 
{MSRDT: '202506291400', MSRRGN_NM: '동북권', MSRSTE_NM: '성동구', PM10: 14, PM25: 13, …}
8
: 
{MSRDT: '202506291400', MSRRGN_NM: '동북권', MSRSTE_NM: '중랑구', PM10: 17, PM25: 12, …}
9
: 
{MSRDT: '202506291400', MSRRGN_NM: '동북권', MSRSTE_NM: '동대문구', PM10: 16, PM25: 10, …}
10
: 
{MSRDT: '202506291400', MSRRGN_NM: '동북권', MSRSTE_NM: '성북구', PM10: 10, PM25: 9, …}
11
: 
{MSRDT: '202506291400', MSRRGN_NM: '동북권', MSRSTE_NM: '도봉구', PM10: 11, PM25: 4, …}
12
: 
{MSRDT: '202506291400', MSRRGN_NM: '동북권', MSRSTE_NM: '강북구', PM10: 13, PM25: 5, …}
13
: 
{MSRDT: '202506291400', MSRRGN_NM: '동북권', MSRSTE_NM: '노원구', PM10: 15, PM25: 10, …}
14
: 
{MSRDT: '202506291400', MSRRGN_NM: '서남권', MSRSTE_NM: '강서구', PM10: 17, PM25: 12, …}
15
: 
{MSRDT: '202506291400', MSRRGN_NM: '서남권', MSRSTE_NM: '구로구', PM10: 13, PM25: 8, …}
16
: 
{MSRDT: '202506291400', MSRRGN_NM: '서남권', MSRSTE_NM: '영등포구', PM10: 15, PM25: 11, …}
17
: 
{MSRDT: '202506291400', MSRRGN_NM: '서남권', MSRSTE_NM: '동작구', PM10: 17, PM25: 9, …}
18
: 
{MSRDT: '202506291400', MSRRGN_NM: '서남권', MSRSTE_NM: '관악구', PM10: 9, PM25: 6, …}
19
: 
{MSRDT: '202506291400', MSRRGN_NM: '서남권', MSRSTE_NM: '금천구', PM10: 13, PM25: 9, …}
20
: 
{MSRDT: '202506291400', MSRRGN_NM: '서남권', MSRSTE_NM: '양천구', PM10: 18, PM25: 10, …}
21
: 
{MSRDT: '202506291400', MSRRGN_NM: '동남권', MSRSTE_NM: '강남구', PM10: 15, PM25: 9, …}
22
: 
{MSRDT: '202506291400', MSRRGN_NM: '동남권', MSRSTE_NM: '서초구', PM10: 28, PM25: 9, …}
23
: 
{MSRDT: '202506291400', MSRRGN_NM: '동남권', MSRSTE_NM: '송파구', PM10: 18, PM25: 14, …}
24
: 
{MSRDT: '202506291400', MSRRGN_NM: '동남권', MSRSTE_NM: '강동구', PM10: 16, PM25: 16, …}
length
: 
25
[[Prototype]]
: 
Array(0)
[[Prototype]]
: 
Object
[[Prototype]]
: 
Object
*/