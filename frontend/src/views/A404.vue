<template>
  <div class='main'>
    <div class='pt-4'>
      <div class='text-center'>404. 존재하지 않는 페이지 입니다 :)</div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'A404',
    data: () => ({
      dynamo_obj: {
        company_id: 1,
        created_date: '1557911402220',
        updated_date: '1557911402220',
        landing_info: {
          landing: {
            manager: 1,
            name: '랜딩 이름',
            title: '브라우저 타이틀',
            header_script: 'console.log()',
            body_script: 'console.log()',
            base_url: 'file_name',
            is_hijack: false,
            hijack_url: null,
            is_active: true,
            is_mobile: false,
            is_banner: false,
            banner_url: null,
            banner_image: null,
            inner_db: true,
            font: 1,
            is_term: false,
            image_term: false,
            show_company: false
          },
          term: {
            title: '',
            content: '',
            image_data: 'assets/image/landing/preview/1557911402220/html/preview.html',
          },
          form: [
            {
              sign: 2,
              name: 'form1',
              bg_color: '#e5ebfa',
              opacity: '7',
              tx_color: '#313131'
            },
            {
              sign: 3,
              name: 'form2',
              bg_color: '#fab6a1',
              opacity: '4',
              tx_color: '#313131'
            }
          ],
          field: [
            {
              back_color: '#287BFF',
              image_data: null,
              name: '이름입력',
              sign: 1,
              holder: '이름을 입력하세요',
              label: false,
              text_color: '#fafafa',
              list: [],
              type: 1,
              form_group_id: 2,
              position: {
                x: 0,
                y: 0,
                w: 100,
                h: 100,
                z: 1
              }
            },
            {
              back_color: '#287BFF',
              image_data: null,
              name: '지점스크롤',
              sign: 3,
              holder: '지점을 선택하세요',
              label: false,
              text_color: '#f0f0f0',
              list: [
                '서울',
                '부산'
              ],
              type: 3,
              form_group_id: 2
            },
            {
              back_color: '#ff6069',
              image_data: null,
              sign: 6,
              name: '홈페이지링크',
              holder: '홈페이지 가기',
              label: true,
              text_color: '#f0f0f0',
              type: 7,
              opacity: 10,
              list: [],
              form_group_id: 2,
              url: 'lcventures.net'
            },
            {
              back_color: '#bfffba',
              image_data: 'assets/image/landing/preview/1557911402220/field/field_1.jpg',
              sign: 7,
              name: '전화걸기',
              holder: '엘씨로 걸기',
              label: true,
              text_color: '#313131',
              type: 8,
              opacity: 10,
              list: [],
              form_group_id: 2,
              value: '0103333333'
            },
            {
              back_color: '#287BFF',
              image_data: null,
              sign: 8,
              name: '취미선택',
              holder: '취미선택',
              label: true,
              text_color: '#f0f0f0',
              type: 5,
              opacity: 10,
              list: [
                '1취미',
                '2취미',
                '3취미'
              ],
              form_group_id: 2
            },


          ],
          sections: [
            [
              {
                type: 1,
                video_type: null,
                form_group_id: null,
                position: {
                  x: 0,
                  y: 0,
                  w: 100,
                  h: 100,
                  z: 1
                },
                image_data: 'assets/image/landing/preview/1557911402220/field/field_1.jpg',
                video_url: null
              }
            ],
            [
              {
                type: 1,
                video_type: null,
                form_group_id: null,
                position: {
                  x: 0,
                  y: 0,
                  w: 100,
                  h: 100,
                  z: 1
                },
                image_data: 'assets/image/landing/preview/1557911402220/field/field_1.jpg',
                video_url: null
              },
              {
                type: 2,
                video_type: null,
                form_group_id: 2,
                section_h: 450,
                position: {
                  x: 0,
                  y: 0,
                  w: 100,
                  h: 100,
                  z: 2
                },
                fields: [
                  {
                    sign: 1,
                    position: {
                      x: 0,
                      y: 0,
                      w: 100,
                      h: 100,
                      z: 2
                    }
                  },
                  {
                    sign: 2,
                    position: {
                      x: 50,
                      y: 0,
                      w: 100,
                      h: 100,
                      z: 3
                    }
                  }
                ],
                image_data: null,
                video_url: null
              }
            ],
            [
              {
                type: 3,
                video_type: 1,
                form_group_id: null,
                position: {
                  x: 0,
                  y: 0,
                  w: 100,
                  h: 100,
                  z: 1
                },
                image_data: null,
                video_url: 'yuMnWsIlEBY'
              }
            ]
          ],
          views: 0
        }
      }
    })
  }
</script>

<style scoped>

</style>
