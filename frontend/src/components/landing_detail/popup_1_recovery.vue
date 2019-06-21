<template>

  <transition name="fade" mode="out-in">

    <!-- When first access for create landing, show the company choice modal -->
    <div class="select_company_wrap" v-show="auto_flag">
      <div class="container company_list_box">

        <h4>임시저장된 랜딩페이지가 있습니다.</h4>

        <div class="form-group row">
          <label class="col-sm-3 col-form-label-sm mt-3" for="auto_id">
            <span>랜딩선택</span>
          </label>

          <div class="col-md-8 mt-sm-3">
            <select class="form-control" name="company" id="auto_id"
                    v-model="recovery">
              <option value="-1">선택하세요</option>
              <option v-for="content in auto_saved" :value="content.LandingNum">
                {{content.landing_info.landing.company_name }} / {{ content.landing_info.landing.init_date }}
              </option>
            </select>
          </div>
          <div class="col-md-1 mt-sm-3 pl-md-0">
            <button type="button" class="btn btn-danger p-md-0 w-100 h-100" @click="auto_saved_delete">삭제</button>
          </div>
        </div>

        <button type="button" class="col btn btn-info mt-3" @click="auto_saved_detail">선택</button>
        <button type="button" class="btn btn-secondary col-12 mt-2" @click="auto_saved_not">선택 안함</button>
        <router-link to="/landing">
          <button type="button" class="btn btn-dark col-12 mt-2">취소</button>
        </router-link>
      </div>
    </div>
  </transition>
</template>

<script>
  export default {
    name: "popup_1_recovery",
    props: [
      'user_obj'
    ],
    data: () => ({
      auto_flag: false,
      company_flag: false,
      recovery: -1,
      auto_saved: [],
    }),
    mounted() {
      // Check if this manager has auto saved landing page
      this.auto_saved_get()
    },
    methods: {
      auto_saved_get() {
        // Check temporary saved landings
        this.auto_saved = []
        this.$store.state.pageOptions.loading = true
        axios.get(this.$store.state.endpoints.baseUrl + 'landing_pages/' + '?marketer=' + this.user_obj.username)
          .then((response) => {
            this.$store.state.pageOptions.loading = false
            let auto_flag = false
            for (let i = 0; i < response.data.length; i++) {
              if (response.data[i].landing_info.landing.name === null) {
                // auto saved list on
                auto_flag = true
                let temp_date = response.data[i].UpdatedTime
                let init_date = new Date(temp_date * 1)
                let date_string = init_date.getFullYear()
                if (init_date.getMonth() < 10) {
                  date_string += '-0' + init_date.getMonth()
                } else {
                  date_string += '-' + init_date.getMonth()
                }
                if (init_date.getDate() < 10) {
                  date_string += '-0' + init_date.getDate()
                } else {
                  date_string += '-' + init_date.getDate()
                }
                response.data[i].landing_info.landing.init_date = date_string
                this.auto_saved.push(response.data[i])
              }
            }
            if (auto_flag == true) {
              this.auto_flag = auto_flag
              this.company_flag = false
            } else {
              this.auto_flag = auto_flag
              this.company_flag = true
            }
          })
          .catch(() => {
            this.$store.state.pageOptions.loading = false
          })
      },
      auto_saved_delete() {
        if (this.recovery != -1) {
          let axios = this.$axios
          let landing_num = this.recovery
          axios.delete(this.$store.state.endpoints.baseUrl + 'landings/api/' + landing_num)
            .then(() => {
              this.recovery = -1
              this.auto_saved_get()
            })
            .catch((error) => {
              console.log(error)
              alert('삭제 중 에러가 발생하였습니다. 다시 시도해주세요.')
            })
        } else {
          alert('삭제 할 페이지를 먼저 선택하세요.')
        }
      },
      auto_saved_not() {
        if (confirm('무시하고 생성하시겠습니까?')) {
          this.$store.state.pageOptions.loading = false
          this.auto_flag = !this.auto_flag
          this.company_flag = !this.company_flag
        }
      },
      auto_saved_detail() {
        if (this.recovery != -1) {
          if (confirm('수정페이지로 이동 하시겠습니까?')) {
            this.$router.currentRoute.meta.protect_leave = 'no'
            this.$router.push({path: '/landings/detail/' + this.recovery})
          }
        } else {
          alert('수정 할 페이지를 먼저 선택하세요.')
        }
      }
    }
  }
</script>

<style scoped>

</style>
