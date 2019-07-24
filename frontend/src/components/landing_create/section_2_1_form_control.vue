<template>

  <div class="form-group row mb-0">

    <!--<div class="alert-info w-100">{{ etc }}</div>-->

    <label class="col-sm-3 col-form-label-sm mt-3" for="form_group">기타 폼 그룹</label>
    <form class="col-sm-9 mt-sm-3 row ml-0" v-on:submit.prevent="form_group_add">
      <input type="text" class="input_one_btn form-control col-md-11" id="form_group" name="form_group"
             placeholder="폼 그룹 이름" maxlength="50" v-model="form_temp">
      <button type="submit" class="btn btn-primary col-md-1 p-0" name="form_group">추가</button>
    </form>

    <label class="col-sm-3 col-form-label-sm mt-3" for="form_group_list"></label>
    <div class="col-sm-9 mt-sm-3 row ml-0">
      <select class="input_one_btn form-control col-md-11" name="form_group_list" id="form_group_list"
              :value="etc_arrow" @change="form_changed($event.target.value * 1)">
        <option value="-1">그룹을 선택하세요</option>
        <option v-for="item in etc" :value.number="item.sign">{{ item.name }}</option>
      </select>
      <button type="button" class="btn btn-danger col-md-1 p-0"
              @click.prevent="form_group_delete(form_selected.sign)">
        삭제
      </button>
    </div>

    <label v-if="etc_arrow * 1 !== -1" class="col-sm-3 col-form-label-sm mt-3" for="form_group_type">폼 타입</label>
    <div v-if="etc_arrow * 1 > 0" class="col-sm-9 mt-sm-3 row ml-0">
      <select class="form-control col-md-12" name="form_group_list" id="form_group_type"
              v-model.number="form_selected.type">
        <option value="-1">그룹을 선택하세요</option>
        <option value="1">링크 버튼</option>
        <option value="2">전화 버튼</option>
      </select>
    </div>

    <label v-if="etc_arrow * 1 !== -1 && form_selected.type == 1" class="col-sm-3 col-form-label-sm mt-3"
           for="form_group_link">링크 url</label>
    <div v-if="etc_arrow * 1 > 0 && form_selected.type == 1" class="col-sm-9 mt-sm-3 row ml-0">
      <input type="text" class="form-control col-md-12" id="form_group_link" v-model="form_selected.link">
    </div>

    <label v-if="etc_arrow * 1 !== -1 && form_selected.type == 2" class="col-sm-3 col-form-label-sm mt-3"
           for="form_group_tel">전화 번호</label>
    <div v-if="etc_arrow * 1 > 0 && form_selected.type == 2" class="col-sm-9 mt-sm-3 row ml-0">
      <input type="tel" class="form-control col-md-12" id="form_group_tel" v-model="form_selected.tel">
    </div>

    <label v-if="etc_arrow * 1 !== -1" class="col-sm-3 col-form-label-sm mt-3" for="form_group_bg">
      폼 배경색
    </label>
    <div v-if="etc_arrow * 1 !== -1" class="col-sm-9 mt-sm-3 row ml-0">
      <div class="color_wrap form-control col-sm-2" id="form_group_bg">
        <input type="color" v-model="form_selected.bg_color" class="color_picker">
      </div>
      <div class="margin_div"></div>
      <input type="text" v-model="form_selected.bg_color" class="form-control col-sm-5" maxlength="10">
    </div>

    <label v-if="etc_arrow * 1 !== -1" class="col-sm-3 col-form-label-sm mt-3" for="opacity_slider">
      배경 불투명도
    </label>
    <div v-if="etc_arrow * 1 !== -1" class="col-sm-9 mt-sm-3 row ml-0">
      <div class="form-control col-sm-2">{{ form_selected.opacity * 10 }}%</div>
      <div class="margin_div"></div>
      <div class="slide_container col-sm-5 form-control border-0 p-0">
        <input class="opacity_slider w-100 h-100" id="opacity_slider" type="range" min="0" max="10" value="10"
               v-model="form_selected.opacity">
      </div>
    </div>

    <label v-if="etc_arrow * 1 !== -1" class="col-sm-3 col-form-label-sm mt-3" for="form_group_col">
      폼 폰트색
    </label>
    <div v-if="etc_arrow * 1 !== -1" class="col-sm-9 mt-sm-3 row ml-0">
      <div class="color_wrap form-control col-sm-2" id="form_group_col">
        <input type="color" v-model="form_selected.tx_color" class="color_picker">
      </div>
      <div class="margin_div"></div>
      <input type="text" v-model="form_selected.tx_color" class="form-control col-sm-5" maxlength="10">
    </div>

    <label v-if="etc_arrow * 1 !== -1" class="col-sm-3 col-form-label-sm mt-3" for="term_img">버튼 이미지 파일</label>
    <div v-if="etc_arrow * 1 !== -1" class="col-sm-9 mt-sm-3 row ml-0">
      <input type="file" class="input_one_btn form-control col-md-11 pt-1" id="term_img" placeholder="이미지"
             ref="term_file_input" @change="etc_file_add($event.target.files[0])" accept="image/*">
      <button type="button" class="btn btn-danger col-md-1 p-0" @click.prevent="etc_file_delete()">삭제</button>
    </div>
    <label v-if="etc_arrow * 1 !== -1" class="col-sm-3 col-form-label-sm mt-3" for="term_img_preview">미리보기</label>
    <div v-if="etc_arrow * 1 !== -1" class="col-sm-9 mt-sm-3 row ml-0" id="term_img_preview">
      <div v-if="form_selected.image_data" class="term_preview_wrap">
        <img class="term_preview" :src="key_to_url(form_selected.image_data)" alt="기타 폼 이미지 미리보기">
      </div>
      <div v-else class="form-control">
        <div>등록된 파일이 없습니다</div>
      </div>
    </div>

    <!--<div class="alert-info">{{ etc }}</div>-->
    <!--<div class="alert-warning">{{ form_selected }}</div>-->

  </div>

</template>

<script>
  export default {
    name: "section_2_form_control_etc",
    props: [
      'etc',
      'etc_arrow',
      'epoch_time',
      'updated_date',
      'push_landing'
    ],
    data: () => ({
      form_obj: [],
      form_temp: '',
      form_selected: {
        sign: -1,
        type: 1,
        tx_color: '#313131',
        bg_color: '#fafafa',
        opacity: '10',
        link: '',
        tel: '',
        image_data: ''
      },
    }),
    mounted() {
      this.form_init()
    },
    methods: {
      form_init() {
        this.form_obj = []
        this.form_obj = this.etc
      },
      form_changed(id) {
        this.form_init()
        this.$emit('update:etc_arrow', id)
        if (id == -1) {
          this.form_selected = {
            sign: -1,
            type: -1,
            tx_color: '#313131',
            bg_color: '#fafafa',
            opacity: '10',
            link: '',
            tel: '',
            image_data: ''
          }
        } else {
          for (let i = 0; i < this.form_obj.length; i++) {
            if (this.form_obj[i].sign == id) {
              this.form_selected = this.form_obj[i]
            }
          }
        }
      },
      form_group_add() {
        // this.form_init()
        if (this.form_temp) {
          let len = this.form_obj.length
          let flag = true
          if (len) {
            for (let i = 0; i < len; i++) {
              if (this.form_obj[i].name === this.form_temp) {
                alert('폼 그룹 이름이 이미 존재합니다.')
                flag = false
                return flag
              }
            }
            if (flag) {
              let highest = 0
              for (let i = 0; i < len; i++) {
                if (this.form_obj[i].sign > highest) {
                  highest = this.form_obj[i].sign
                }
              }
              this.form_obj.push({
                sign: highest + 1,
                name: this.form_temp,
                type: -1,
                bg_color: '#fafafa',
                tx_color: '#313131',
                opacity: '10',
                link: '',
                tel: '',
                image_data: ''
              })
              this.form_temp = ''
              this.$emit('update:etc', this.form_obj)
              alert('폼 그룹이 생성되었습니다.')
              this.push_landing()
            }
          } else {
            this.form_obj.push({
              sign: 1,
              name: this.form_temp,
              type: -1,
              bg_color: '#fafafa',
              tx_color: '#313131',
              opacity: '10',
              link: '',
              tel: '',
              image_data: ''
            })
            this.form_temp = ''
            this.$emit('update:etc', this.form_obj)
            alert('폼 그룹이 생성되었습니다.')
            this.push_landing()
            this.form_init()
          }
        } else {
          alert('폼 그룹 이름을 입력하세요!')
        }
      },
      form_group_delete(id) {
        // this.form_init()
        if (id !== -1) {
          if (confirm('이 폼그룹을 삭제하시겠습니까?')) {
            this.form_init()
            this.form_obj = this.form_obj.filter(el => el.sign != id)
            // this.form_arrow = -1
            this.$emit('update:etc_arrow', -1)
            this.$emit('update:etc', this.form_obj)
            this.form_selected = {
              sign: -1,
              type: -1,
              tx_color: '#313131',
              bg_color: '#fafafa',
              opacity: '10',
              link: '',
              tel: '',
              image_data: ''
            }
            this.form_init()
            // Field objs delete also
            // this.field_work(id)
            this.push_landing()
          }
        } else {
          alert('그룹을 먼저 선택하세요.')
        }
      },
      etc_file_add(file) {
        if (this.etc_arrow > -1) {
          this.form_init()
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

          if (this.form_selected.image_data) {
            s3.deleteObject({
              Key: this.form_selected.image_data
            }, (err, data) => {
              if (err) {
                alert('There was an error deleting your photo: ', err.message)
              } else {
                this.form_selected.image_data = null
              }
            })
          }

          let params = {}

          if (this.updated_date) {
            params = {
              Key: 'assets/images/landing/' + this.epoch_time + '/etc/' + Date.now() + '_' + file.name,
              ContentType: file.type,
              Body: file,
              ACL: 'public-read'
            }
          } else {
            params = {
              Key: 'assets/images/landing/preview/' + this.epoch_time + '/etc/' + Date.now() + '_' + file.name,
              ContentType: file.type,
              Body: file,
              ACL: 'public-read'
            }
          }

          s3.upload(params, (error, data) => {
            if (error) {
              console.log('S3 method error occurred', error)
            } else {
              // console.log('S3 method success', data)
              this.form_selected.image_data = params.Key
              this.$emit('update:etc', this.form_obj)
              this.push_landing()
            }
          })

        }

      },
      etc_file_delete() {

        if (this.etc_arrow > -1) {
          this.form_init()
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

          let photoKey = this.form_selected.image_data

          if (photoKey) {
            s3.deleteObject({Key: photoKey}, (err, data) => {
              if (err) {
                alert('이미지 삭제 중 오류가 발생하였습니다: ', err.message)
              } else {
                // alert('Successfully deleted photo.', data)
                document.getElementById('term_img').value = ''
                this.form_selected.image_data = null
                this.$emit('update:etc', this.form_obj)

                this.push_landing()
              }
            })
          }
        }


      },
      key_to_url(key) {
        if (key != null) {
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
        } else {
          return ''
        }
      }
    }
  }
</script>

<style scoped>
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
