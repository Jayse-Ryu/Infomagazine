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
              sign: 1,
              type: 1,
              back_color: '#287BFF',
              image_data: null,
              name: 'non label',
              holder: 'non label 입니다.',
              label: false,
              text_color: '#fafafa',
              list: [],
              form_group_id: 1,
              url: ''
            },
            {
              sign: 2,
              type: 9,
              back_color: '#ff6069',
              image_data: null,
              name: '완료버튼',
              holder: '신청하기',
              label: true,
              text_color: '#f0f0f0',
              list: [],
              form_group_id: 2,
              url: ''
            },
            {
              sign: 3,
              type: 1,
              back_color: '#287BFF',
              image_data: null,
              name: '필드있음',
              holder: '라벨트루',
              label: true,
              text_color: '#f0f0f0',
              list: [],
              form_group_id: 1,
              url: 'link.com'
            },
            {
              sign: 4,
              type: 9,
              back_color: '#ff6069',
              image_data: null,
              name: '완료버튼',
              holder: '신청하기',
              label: true,
              text_color: '#f0f0f0',
              list: [],
              form_group_id: 2,
              url: ''
            }
          ],
          sections: [
            [
              {
                type: 1,
                video_type: null,
                form_group_id: null,
                fields: [],
                position: {
                  x: 0,
                  y: 0,
                  w: 1000,
                  h: 750,
                  z: 1
                },
                image_data: '1000x750',
                video_url: null
              },
              {
                type: 2,
                video_type: null,
                form_group_id: 1,
                fields: [
                  {
                    sign: 1,
                    position: {
                      x: 50,
                      y: 100,
                      w: 400,
                      h: 50,
                      z: 1,
                    }
                  },
                  {
                    sign: 2,
                    position: {
                      x: 150,
                      y: 200,
                      w: 200,
                      h: 50,
                      z: 1,
                    }
                  }
                ],
                position: {
                  x: 200,
                  y: 500,
                  w: 600,
                  h: 250,
                  z: 2
                },
                image_data: null,
                video_url: null
              }
            ],
            [
              {
                type: 1,
                video_type: null,
                form_group_id: null,
                fields: [],
                position: {
                  x: 0,
                  y: 0,
                  w: 1000,
                  h: 850,
                  z: 1
                },
                image_data: '1000x850',
                video_url: null
              },
              {
                type: 1,
                video_type: null,
                form_group_id: null,
                fields: [],
                position: {
                  x: 200,
                  y: 200,
                  w: 250,
                  h: 150,
                  z: 2
                },
                image_data: '250x150',
                video_url: null
              },
              {
                type: 1,
                video_type: null,
                form_group_id: null,
                fields: [],
                position: {
                  x: 550,
                  y: 200,
                  w: 250,
                  h: 150,
                  z: 2
                },
                image_data: '250x150',
                video_url: null
              },
              {
                type: 2,
                video_type: null,
                form_group_id: 2,
                fields: [
                  {
                    sign: 3,
                    position: {
                      x: 50,
                      y: 100,
                      w: 500,
                      h: 50,
                      z: 1,
                    }
                  },
                  {
                    sign: 4,
                    position: {
                      x: 200,
                      y: 350,
                      w: 400,
                      h: 50,
                      z: 1,
                    }
                  }
                ],
                position: {
                  x: 200,
                  y: 450,
                  w: 600,
                  h: 350,
                  z: 2
                },
                image_data: null,
                video_url: null
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
