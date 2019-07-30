<template>
  <div class="form-group row mb-0">

    <label class="col-sm-3 col-form-label-sm mt-3" for="layout_font">
      <span>레이아웃 폰트</span>
    </label>
    <div class="col-sm-9 mt-sm-3 row ml-0">
      <select class="form-control" name="layout_font" id="layout_font"
              v-model.number="landing.font">
        <option value="-1">OS 기본</option>
        <option value="1">Sans-serif</option>
        <option value="2">나눔고딕 (Nanum Gothic)</option>
        <option value="3">나눔명조 (Nanum Myeongjo)</option>
        <option value="4">제주고딕 (Jeju Gothic)</option>
      </select>
    </div>

    <!--<label class="col-sm-3 col-form-label-sm mt-3" for="in_db">
      <span>레이아웃 내 DB</span>
      <span class="question badge btn-secondary p-1 align-middle" v-if="window_width > 768"
            v-tooltip="{
                      content: msg.in_db,
                      placement: 'right',
                      offset: 5,
                      trigger: 'hover',
                      }">?</span>
      <span class="question badge btn-secondary p-1 align-middle" v-else
            v-tooltip="{
                      content: msg.in_db,
                      placement: 'right',
                      offset: 5,
                      trigger: 'click',
                      }">?</span>
    </label>
    <div class="col-sm-9 mt-sm-3">
      <label class="switch" for="in_db">
        <input type="checkbox" id="in_db" v-model="landing.inner_db">
        <span class="slider round"></span>
      </label>
    </div>-->

    <!--<label class="col-sm-3 col-form-label-sm mt-3" for="in_company">
      <span>사업자 표기</span>
      <span class="question badge btn-secondary p-1 align-middle" v-if="window_width > 768"
            v-tooltip="{
                      content: msg.in_company,
                      placement: 'right',
                      offset: 5,
                      trigger: 'hover',
                      }">?</span>
      <span class="question badge btn-secondary p-1 align-middle" v-else
            v-tooltip="{
                      content: msg.in_company,
                      placement: 'right',
                      offset: 5,
                      trigger: 'click',
                      }">?</span>
    </label>
    <div class="col-sm-9 mt-sm-3">
      <label class="switch" for="in_company">
        <input type="checkbox" id="in_company" v-model="landing.show_company">
        <span class="slider round"></span>
      </label>
    </div>-->

    <label class="col-sm-3 col-form-label-sm mt-3" for="is_hijack">
      <span>후팝업</span>
      <span class="question badge btn-secondary p-1 align-middle" v-if="window_width > 768"
            v-tooltip="{
                      content: msg.hijack,
                      placement: 'right',
                      offset: 5,
                      trigger: 'hover',
                      }">?</span>
      <span class="question badge btn-secondary p-1 align-middle" v-else
            v-tooltip="{
                      content: msg.hijack,
                      placement: 'right',
                      offset: 5,
                      trigger: 'click',
                      }">?</span>
    </label>
    <div class="col-sm-9 mt-sm-3">
      <label class="switch" for="is_hijack">
        <input type="checkbox" id="is_hijack" v-model="landing.is_hijack">
        <span class="slider round"></span>
      </label>
    </div>
    <label v-if="landing.is_hijack" class="col-sm-3 col-form-label-sm mt-3"
           for="hijack">
      <span>후팝업 링크</span>
    </label>
    <div v-if="landing.is_hijack" class="col-sm-9 mt-sm-3 row ml-0">
      <input type="text" class="form-control col" id="hijack" placeholder="후팝업 주소"
             v-model="landing.hijack_url">
      <hr>
    </div>

    <label class="col-sm-3 col-form-label-sm mt-3" for="in_banner">
      <span>띠배너</span>
      <span class="question badge btn-secondary p-1 align-middle" v-if="window_width > 768"
            v-tooltip="{content: msg.in_banner,
                      placement: 'right',
                      offset: 5,
                      trigger: 'hover',
                      }">?</span>
      <span class="question badge btn-secondary p-1 align-middle" v-else
            v-tooltip="{content: msg.in_banner,
                      placement: 'right',
                      offset: 5,
                      trigger: 'click',
                      }">?</span>
    </label>
    <div class="col-sm-9 mt-sm-3">
      <label class="switch" for="in_banner">
        <input type="checkbox" id="in_banner" v-model="landing.is_banner">
        <span class="slider round"></span>
      </label>
    </div>

    <label v-if="landing.is_banner" class="col-sm-3 col-form-label-sm mt-3"
           for="in_banner_img">
      <span>띠배너 옵션</span>
    </label>
    <div v-if="landing.is_banner" class="col-sm-9 mt-sm-3 row ml-0">

      <input type="file" class="form-control col-sm-5 col-md-5 pt-1" id="in_banner_img" placeholder="이미지"
             ref="in_banner_file_input" @change="in_banner_file_add($event.target.files[0])" accept="image/*">
      <div class="margin_div"></div>
      <input type="text" class="form-control col-sm-7 col-md-5" id="in_banner_desc" placeholder="띠배너 주소"
             v-model="landing.banner_url">
      <div class="margin_div"></div>
      <!--<button type="button" class="btn btn-primary col-md-1 p-0">추가</button>-->
      <button type="button" class="btn btn-danger col-md-1 p-0" @click.prevent="in_banner_file_delete()">
        <span>삭제</span>
      </button>
    </div>
    <label v-if="landing.is_banner" class="col-sm-3 col-form-label-sm mt-3" for="term_img_preview">미리보기</label>
    <div v-if="landing.is_banner" class="col-sm-9 mt-sm-3 row ml-0" id="term_img_preview">
      <div v-if="landing.banner_image" class="term_preview_wrap">
        <img class="term_preview" :src="landing.banner_image" alt="배너 이미지 미리보기">
      </div>
      <div v-else class="form-control">
        <div>등록된 파일이 없습니다</div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "section_7_layout_opt",
    props: [
      'window_width',
      'epoch_time',
      'page_id',
      'updated_date',
      'landing',
      'push_landing'
    ],
    data: () => ({
      msg: {
        in_db: '레이아웃 내부에 DB 폼 그룹을 위치시키거나 하단 팝업으로 대체합니다.',
        in_company: '랜딩 페이지에 하단 Footer로 해당 고객업체의 정보를 자동 기입합니다.',
        hijack: '사용자가 뒤로 가기 시 해당 링크로 강제 이동시킵니다.',
        in_banner: '스크롤 시 따라다니는 배너를 생성합니다.'
      }
    }),
    mounted() {

    },
    methods: {
      in_banner_file_add(file) {
        /* When file data changed */
        /* When file data changed */
        let key = require('../../../vue_env')

        AWS.config.update({
          region: key.BucketRegion,
          credentials: new AWS.CognitoIdentityCredentials({
            IdentityPoolId: key.IdentityPoolId
          })
        })

        let s3 = new AWS.S3(
          {
            apiVersion: '2008-10-17',
            params: {
              Bucket: key.AWS_STORAGE_BUCKET_NAME
            }
          }
        )

        if (this.landing.banner_image) {

          s3.deleteObject({Key: this.landing.banner_image.replace('https://assets.infomagazine.xyz', 'assets')}, (err, data) => {
            if (err) {
              alert('There was an error deleting your photo: ', err.message)
            } else {
              this.landing.banner_image = null
            }
          })

        }

        let params = {}

        params = {
          Key: 'assets/images/landing/' + this.page_id + '/banner/' + file.name + '_' + Date.now(),
          ContentType: file.type,
          Body: file
        }

        s3.upload(params, (error, data) => {
          if (error) {
            console.log('S3 method error occurred', error)
          } else {
            // console.log('S3 method success', data)
            this.landing.banner_image = params.Key.replace('assets/', 'https://assets.infomagazine.xyz/')
            this.push_landing()
          }
        })
      },
      in_banner_file_delete() {

        let key = require('../../../vue_env')

        AWS.config.update({
          region: key.BucketRegion,
          credentials: new AWS.CognitoIdentityCredentials({
            IdentityPoolId: key.IdentityPoolId
          })
        })

        let s3 = new AWS.S3(
          {
            apiVersion: '2008-10-17',
            params: {
              Bucket: key.AWS_STORAGE_BUCKET_NAME
            }
          }
        )

        let photoKey = this.landing.banner_image.replace('https://assets.infomagazine.xyz', 'assets')

        if (photoKey) {
          s3.deleteObject({Key: photoKey}, (err, data) => {
            if (err) {
              alert('이미지 삭제 중 오류가 발생하였습니다: ', err.message)
            } else {
              // alert('Successfully deleted photo.', data)
              document.getElementById('in_banner_img').value = ''
              this.landing.banner_image = null

              this.push_landing()
            }
          })
        }
      },
      // key_to_url(key) {
      //   if (key) {
      //     if (key.indexOf('assets') > -1) {
      //       let divided = key.split('/')
      //       let url = 'https://'
      //
      //       if (this.updated_date == '') {
      //         url += 'infomagazine.s3.ap-northeast-2.amazonaws.com/' + key
      //       } else {
      //         for (let i = 0; i < divided.length; i++) {
      //           if (i == 0) {
      //             url += (divided[i] + '.infomagazine.xyz')
      //             // url += ('assets' + '.infomagazine.xyz')
      //           } else {
      //             url += ('/' + divided[i])
      //           }
      //         }
      //       }
      //       return url
      //     } else {
      //       let divided = key.split('/')
      //       let url = 'https://'
      //
      //       if (this.updated_date == '') {
      //         url += 'infomagazine.s3.ap-northeast-2.amazonaws.com/assets' + key
      //       } else {
      //         for (let i = 0; i < divided.length; i++) {
      //           if (i == 0) {
      //             // url += (divided[i] + '.infomagazine.xyz')
      //             url += ('assets' + '.infomagazine.xyz')
      //           } else {
      //             url += ('/' + divided[i])
      //           }
      //         }
      //       }
      //       return url
      //     }
      //   } else {
      //     return ''
      //   }
      //
      // }
    }
  }
</script>

<style lang="scss" scoped>
  .term_preview_wrap {
    display: block;
    width: 100%;
    padding: .375rem .75rem;
    font-size: 1rem;
    line-height: 1.5;
    color: #495057;
    background-color: #fff;
    background-clip: padding-box;
    border: 1px solid #ced4da;
    border-radius: .25rem;
    transition: border-color .15s ease-in-out, box-shadow .15s ease-in-out;
    text-align: center;
  }

  .term_preview {
    position: relative;
    max-width: 100%;
  }
</style>
