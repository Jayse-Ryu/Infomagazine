<template>
  <div class="form-group row">

    <label class="col-sm-3 col-form-label-sm mt-3" for="company_name">
      <span>고객업체*</span>
    </label>

    <div class="col-sm-9 mt-sm-3" id="company_name">

      <select class="form-control" name="company_name" v-model="dynamo_obj.LandingInfo.landing.company">
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
      <input type="text" :class="duplicated_name_class" id="landing" maxlength="50"
             v-model="dynamo_obj.LandingInfo.landing.name" @change="check_name">
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
      <input type="text" :class="duplicated_url_class" id="base_url" maxlength="30"
             v-model="dynamo_obj.LandingInfo.landing.base_url" @change="check_url">
    </div>

  </div>
</template>

<script>
  export default {
    name: "section_1_required",
    data: () => ({}),
    mounted() {
      axios.get(this.$store.state.endpoints.baseUrl + 'companies/')
        .then((response) => {
          console.log('companies well loaded ? ', response)

        })
        .catch((error) => {
          console.log(error)
        })
    },
    methods: {}
  }
</script>

<style lang="scss" scoped>

</style>
