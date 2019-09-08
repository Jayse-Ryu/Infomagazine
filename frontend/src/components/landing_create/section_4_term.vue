<template>
  <div>

    <div class="form-group row mb-0">

      <label class="col-sm-3 col-form-label-sm mt-3" for="term_status">약관</label>

      <div class="col-sm-9 mt-sm-3">
        <label class="switch" for="term_status">
          <input type="checkbox" id="term_status" v-model="landing.is_term"
                 @change="push_landing()">
          <span class="slider round"></span>
        </label>
      </div>

      <label v-if="landing.is_term" class="col-sm-3 col-form-label-sm mt-3"
             for="term_switch">
        약관 이미지
      </label>

      <div v-if="landing.is_term" class="col-sm-9 mt-sm-3">
        <label class="switch" for="term_switch">
          <input type="checkbox" id="term_switch" v-model="landing.image_term"
                 @change="push_landing()">
          <span class="slider round"></span>
        </label>
      </div>

    </div>

    <div class="form-group row"
         v-if="landing.is_term && landing.image_term">
      <label class="col-sm-3 col-form-label-sm mt-3" for="term_img">약관 이미지 파일</label>
      <div class="col-sm-9 mt-sm-3 row ml-0">
        <input type="file" class="input_one_btn form-control col-md-11 pt-1" id="term_img" placeholder="이미지"
               ref="term_file_input" @change="term_file_add($event.target.files[0])" accept="image/*">
        <button type="button" class="btn btn-danger col-md-1 p-0" @click.prevent="term_file_delete()">삭제</button>
      </div>
      <label class="col-sm-3 col-form-label-sm mt-3" for="term_img_preview">미리보기</label>
      <div class="col-sm-9 mt-sm-3 row ml-0" id="term_img_preview">
        <div v-if="term.image_data" class="term_preview_wrap">
          <img class="term_preview" :src="term.image_data" alt="약관 이미지 미리보기">
        </div>
        <div v-else class="form-control">
          <div>등록된 파일이 없습니다</div>
        </div>
      </div>
    </div>

    <div class="form-group row"
         v-if="landing.is_term && !landing.image_term">
      <label class="col-sm-3 col-form-label-sm mt-3" for="term_title">약관 url</label>
      <div class="col-sm-9 mt-sm-3">
        <input type="text" class="form-control" id="term_url" placeholder="약관 url"
               v-model="term.url" @change="push_landing()">
      </div>
      <label class="col-sm-3 col-form-label-sm mt-3" for="term_title">약관 제목</label>
      <div class="col-sm-9 mt-sm-3">
        <input type="text" class="form-control" id="term_title" placeholder="약관 제목"
               v-model="term.title" @change="push_landing()">
      </div>
      <label class="col-sm-3 col-form-label-sm mt-3" for="term_cont">약관 내용</label>
      <div class="col-sm-9 mt-sm-3">
          <textarea type="text" class="form-control" id="term_cont" rows="4" placeholder="약관 내용"
                    v-model="term.content" @change="push_landing()"></textarea>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "section_3_term",
    props: [
      'epoch_time',
      'page_id',
      'updated_date',
      'landing',
      'term',
      'push_landing'
    ],
    methods: {
      term_file_add(file) {
        /* When file data changed */

        AWS.config.update({
          region: process.env.VUE_APP_ENV_BucketRegion,
          credentials: new AWS.CognitoIdentityCredentials({
            IdentityPoolId: process.env.VUE_APP_ENV_IdentityPoolId
          })
        })

        let s3 = new AWS.S3(
          {
            apiVersion: '2008-10-17',
            params: {
              Bucket: process.env.VUE_APP_ENV_AWS_STORAGE_BUCKET_NAME
            }
          }
        )

        if (this.term.image_data) {
          let photo_key = this.term.image_data.replace('https://assets.infomagazine.xyz', 'assets')
          s3.deleteObject({Key: photo_key}, (err, data) => {
            if (err) {
              alert('There was an error deleting your photo: ', err.message)
            } else {
              this.term.image_data = null
            }
          })

        }

        let params = {}

        let file_name = file.name.split('.')[0] + '_' + Date.now() + '.' + file.name.split('.')[1]

        params = {
          Key: 'assets/images/landing/' + this.page_id + '/term/' + file_name,
          ContentType: file.type,
          Body: file
        }

        s3.upload(params, (error, data) => {
          if (error) {
            console.log('S3 method error occurred', error)
          } else {
            // console.log('S3 method success', data)
            this.term.image_data = params.Key.replace('assets/', 'https://assets.infomagazine.xyz/')
            this.push_landing()
          }
        })
      },
      term_file_delete() {

        AWS.config.update({
          region: process.env.VUE_APP_ENV_BucketRegion,
          credentials: new AWS.CognitoIdentityCredentials({
            IdentityPoolId: process.env.VUE_APP_ENV_IdentityPoolId
          })
        })

        let s3 = new AWS.S3(
          {
            apiVersion: '2008-10-17',
            params: {
              Bucket: process.env.VUE_APP_ENV_AWS_STORAGE_BUCKET_NAME
            }
          }
        )

        let photoKey = this.term.image_data.replace('https://assets.infomagazine.xyz', 'assets')

        if (photoKey) {
          s3.deleteObject({Key: photoKey}, (err, data) => {
            if (err) {
              alert('이미지 삭제 중 오류가 발생하였습니다: ', err.message)
            } else {
              // alert('Successfully deleted photo.', data)
              document.getElementById('term_img').value = ''
              this.term.image_data = null

              this.push_landing()
            }
          })
        }

      },
      // key_to_url(key) {
      //   if (key != null) {
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
