<template>
  <div>

    <div class="form-group row mb-0">

      <label class="col-sm-3 col-form-label-sm mt-3" for="term_status">약관</label>

      <div class="col-sm-9 mt-sm-3">
        <label class="switch" for="term_status">
          <input type="checkbox" id="term_status" v-model="term_state"
                 @change="change_switch('term')">
          <span class="slider round"></span>
        </label>
      </div>

      <label v-if="term_state" class="col-sm-3 col-form-label-sm mt-3"
             for="term_switch">
        약관 이미지
      </label>

      <div v-if="term_state" class="col-sm-9 mt-sm-3">
        <label class="switch" for="term_switch">
          <input type="checkbox" id="term_switch" v-model="image_state"
                 @change="change_switch('image')">
          <span class="slider round"></span>
        </label>
      </div>

    </div>

    <div class="form-group row"
         v-if="term_state && image_state">
      <label class="col-sm-3 col-form-label-sm mt-3" for="term_img">약관 이미지 파일</label>
      <div class="col-sm-9 mt-sm-3 row ml-0">
        <input type="file" class="input_one_btn form-control col-md-11 pt-1" id="term_img" placeholder="이미지"
               ref="term_file_input" @change="term_file_add($event.target.files[0])" accept="image/*">
        <button type="button" class="btn btn-danger col-md-1 p-0" @click.prevent="term_file_delete()">삭제</button>
      </div>
      <label class="col-sm-3 col-form-label-sm mt-3" for="term_img_preview">약관 이미지 미리보기</label>
      <div class="col-sm-9 mt-sm-3 row ml-0" id="term_img_preview">
        <div v-if="term.image_data" class="term_preview_wrap">
          <img class="term_preview" :src="key_to_url(term.image_data)" alt="약관 이미지 미리보기">
        </div>
        <div v-else class="form-control">
          <div>등록된 파일이 없습니다</div>
        </div>
      </div>
    </div>

    <div class="form-group row"
         v-if="term_state && !image_state">
      <label class="col-sm-3 col-form-label-sm mt-3" for="term_title">약관 제목</label>
      <div class="col-sm-9 mt-sm-3">
        <input type="text" class="form-control" id="term_title" placeholder="title"
               v-model="term.title" @change="push_landing()">
      </div>
      <label class="col-sm-3 col-form-label-sm mt-3" for="term_cont">약관 내용</label>
      <div class="col-sm-9 mt-sm-3">
          <textarea type="text" class="form-control" id="term_cont" rows="4" placeholder="content"
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
      'term_switch',
      'image_switch',
      'term',
      'push_landing'
    ],
    data: () => ({
      term_state: false,
      image_state: false
    }),
    mounted() {
      this.init_switch()
    },
    methods: {
      init_switch() {
        this.term_state = this.term_switch
        this.image_state = this.image_switch
      },
      change_switch(option) {
        if (option == 'term') {
          this.$emit('update:term_switch', this.term_state)
          this.push_landing()
        } else if (option == 'image') {
          this.$emit('update:image_switch', this.image_state)
          this.push_landing()
        }

      },
      term_file_add(file) {
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

        let params = {
          Key: 'assets/images/landing/preview/' + this.epoch_time + '/term/' + file.lastModified + '_' + file.name,
          ContentType: file.type,
          Body: file,
          ACL: 'public-read'
        }

        s3.upload(params, (error, data) => {
          if (error) {
            console.log('S3 method error occurred', error)
          } else {
            // console.log('S3 method success', data)
            this.term.image_data = params.Key
            this.push_landing()
          }
        })
      },
      term_file_delete() {

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

        let photoKey = this.term.image_data

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
      key_to_url(key) {
        let divided = key.split('/')
        let url = 'https://'

        if (this.updated_date == '') {
          url += 'infomagazine.s3.ap-northeast-2.amazonaws.com/' + key
        } else {
          for (let i = 0; i < divided.length; i++) {
            if (i == 0) {
              url += (divided[i] + '.infomagazine.xyz')
            } else {
              url += ('/' + divided[i])
            }
          }
        }

        return url
      }
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
