<template>
  <div class="form-group row">

    <label class="col-sm-3 col-form-label-sm mt-3" for="company_name">
      <span>고객업체*</span>
    </label>

    <div class="col-sm-9 mt-sm-3" id="company_name">
      <select class="form-control" name="company_name" v-model="dynamo.company_id"
              @change="company_change()">
        <option value="-1">업체를 선택하세요</option>
        <option v-for="content in landing_company" :value="content.id">
          {{ content.corp_name }} - {{ content.corp_sub_name }}
        </option>
      </select>

    </div>

    <label class="col-sm-3 col-form-label-sm mt-3" for="landing">
      <span>랜딩페이지 이름*</span>
    </label>
    <div class="col-sm-9 mt-sm-3">
      <input type="text" :class="error_label.class.name" id="landing" maxlength="50"
             :value="name" @change="check_name" @keyup="$emit('update:name', $event.target.value)">
    </div>

    <label class="col-sm-3 col-form-label-sm mt-3" for="base_url">
      <span>메인 URL*</span>
      <span class="question badge btn-secondary p-1 align-middle" v-if="window_width > 768"
            v-tooltip="{
                  content: msg.base_url,
                  placement: 'right',
                  offset: 5,
                  trigger: 'hover',
                  }">?</span>
      <span class="question badge btn-secondary p-1 align-middle" v-else
            v-tooltip="{
                  content: msg.base_url,
                  placement: 'right',
                  offset: 5,
                  trigger: 'click',
                  }">?</span>
    </label>
    <div class="col-sm-9 mt-sm-3">
      <input type="text" :class="error_label.class.base_url" id="base_url" maxlength="30"
             :value="base_url" @change="check_url"
             @keyup="$emit('update:base_url', $event.target.value)">
    </div>

    <label class="col-sm-3 col-form-label-sm mt-3" for="db_show">
      <span>DB 조회</span>
    </label>
    <div class="col-sm-9 mt-sm-3">
      <router-link :to="'/db/detail/' + page_id">
        <button type="button" id="db_show" class="col-sm-12 btn btn-info">DB 보기</button>
      </router-link>
    </div>

  </div>
</template>

<script>
  export default {
    name: "section_1_basic",
    props: [
      'window_width',
      'dynamo',
      'page_id',
      'company',
      'name',
      'base_url',
      'error_name',
      'error_base_url',
      'push_landing'
    ],
    data: () => ({

      // Mounted company list
      landing_company: [],
      // Tooltip message
      msg: {
        base_url: '기본 주소를 지정합니다.'
      },
      // Validation visualizer
      error_label: {
        class: {
          name: 'form-control',
          base_url: 'form-control'
        }
      }
    }),
    mounted() {
      // Get companies for select
      this.get_company()
    },
    methods: {
      get_company() {
        axios.get(this.$store.state.endpoints.baseUrl + 'companies/')
          .then((response) => {
            this.landing_company = response.data.data.results
          })
          .catch((error) => {
            console.log('get companies error', error)
          })
      },
      company_change() {
        this.$emit('update:company', this.dynamo.company_id)
        this.push_landing()
      },
      check_name() {
        if (this.name == '') {
          this.error_label.class.name = 'form-control'
          this.$emit('update:error_name', true)
        } else {
          axios.get(this.$store.state.endpoints.baseUrl + 'landing_pages/')
            .then((response) => {
              for (let i = 0; i < response.data.length; i++) {
                if (response.data[i].landing_info['landing']['name'] !== null) {
                  if ((this.name).toLowerCase() == (response.data[i].landing_info.landing.name).toLowerCase()) {
                    this.error_label.class.name = 'form-control alert-danger'
                    this.$emit('update:error_name', true)
                    return false
                  }
                }
              }
              this.error_label.class.name = 'form-control alert-success'
              this.$emit('update:error_name', false)
              this.push_landing()
            })
        }
      },
      check_url() {
        if (this.base_url == '') {
          this.error_label.class.base_url = 'form-control'
          this.$emit('update:error_base_url', true)
        } else {
          axios.get(this.$store.state.endpoints.baseUrl + 'landing_pages/')
            .then((response) => {
              for (let i = 0; i < response.data.length; i++) {
                if (response.data[i].landing_info['landing']['base_url'] !== null || response.data[i].landing_info['landing']['base_url'] !== '') {
                  if ((this.base_url).toLowerCase() == (response.data[i].landing_info['landing']['base_url']).toLowerCase()) {
                    this.error_label.class.base_url = 'form-control alert-danger'
                    this.$emit('update:error_base_url', true)
                    return false
                  }
                }
              }
              this.error_label.class.base_url = 'form-control alert-success'
              this.$emit('update:error_base_url', false)
              this.push_landing()
            })
        }
      }
    }
  }
</script>

<style lang="scss" scoped>

</style>
