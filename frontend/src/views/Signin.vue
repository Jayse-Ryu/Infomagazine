<template>
  <div>
    <div class="main" id="main_signin">
    </div>

    <!-- Login fields login button signup button logo -->
    <div class="login_box container">
      <div class="login_border">
        <div class="logo_wrap">
          <router-link to="/">
            <div class="logo"><img src="../assets/logo3.png" alt="Logo"></div>
          </router-link>
        </div>

        <form class="login_form form-horizontal" id="LoginForm" @submit.prevent="login">
          <div class="form-group">
            <label for="id_username" class="col-sm-12 control-label">이메일</label>
            <div class="col-sm-12">
              <input class="form-control"
                     required
                     v-model="email"
                     type="text"
                     placeholder="이메일을 입력해주세요."
                     autofocus="autofocus"
                     maxlength="150"
                     id="id_username">
            </div>
          </div>
          <div class="form-group">
            <label for="id_password" class="col-sm-12 control-label">비밀번호</label>
            <div class="col-sm-12">
              <input class="form-control"
                     required
                     v-model="password"
                     type="password"
                     placeholder="비밀번호를 입력해주세요."
                     id="id_password">
            </div>
          </div>
          <div class="form-group">
            <div class="col-12">
              <button type="submit" class="submit_btn btn btn-info col-12 mt-4 mb-2">로그인</button>
              <router-link to="signup" class="btn btn-link col-12">회원가입</router-link>
            </div>
          </div>
        </form>
      </div>

      <div class="warn_wrap">
      <div class="warn_content">
        <ol>
          <li>• 본 사이트는 인포맥 디비시스템 사이트로써 관련자가 아닌 사람은 사용하실 수 없습니다.</li>
          <li>• 관계자가 아닌 사람이 부정 사용 시 법적 제제 및 민형사 상의 처벌을 받을 수 있음을 알립니다.</li>
        </ol>
        <div class="copy_right">Copyright© infomag DB system Inc. All Rights Reserved</div>
      </div>
    </div>

    </div>



  </div>
</template>

<script>
  export default {
    name: 'sign_in',
    data: () => ({
      email: '',
      password: ''
    }),
    mounted() {
      this.$store.state.pageOptions.header = false
      // get id from url
    },
    destroyed() {
      this.$store.state.pageOptions.header = true
    },
    methods: {
      login() {
        const payload = {
          email: this.email,
          password: this.password
        }
        this.$store.state.pageOptions.loading = true
        axios.post(this.$store.state.endpoints.obtainJWT, payload)
          .then((response) => {
            // Axios then
            return this.$store.dispatch('obtainToken', response.data)
          })
          .then(() => {
            // Dispatch then
            this.$store.state.pageOptions.loading = false
            this.$router.push({name: 'gateway'})
          })
          .catch((error) => {
            // Check the account or password
            alert('아이디와 비밀번호를 확인해주세요.')
            document.getElementById('id_password').value = ''
            document.getElementById('id_password').focus()
            this.$store.state.pageOptions.loading = false
            console.log('로그인에 문제가 생겼습니다.', error)
          })
      }
    }
  }
</script>

<style scoped lang="scss">

  @keyframes Gradient {
    0% {
      background-position: 75% 100%
    }
    14% {
      background-position: 20% 50%
    }
    28% {
      background-position: 100% 20%
    }
    42% {
      background-position: 50% 10%
    }
    56% {
      background-position: 90% 50%
    }
    70% {
      background-position: 65% 80%
    }
    86% {
      background-position: 90% 10%
    }
    100% {
      background-position: 75% 100%
    }
  }

  .main {
    position: fixed;
    width: 100%;
    height: 100%;
    max-width: none !important;
    top: 0;
    z-index: -1;
    overflow: auto;
    background: linear-gradient(217deg, rgba(2, 0, 36, .8), rgba(255, 0, 0, 0) 70.71%),
    linear-gradient(127deg, rgba(185, 169, 141, .8), rgba(0, 255, 0, 0) 70.71%),
    linear-gradient(336deg, rgba(0, 212, 255, .8), rgba(0, 0, 255, 0) 70.71%);
    background-size: 180% 180%;
    animation: Gradient 18s ease-in-out infinite;
  }

  .login_box {
    position: absolute;
    top: 47%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 100%;
    font-family: 'Nanum Gothic', 'sans-serif';
    max-width: 500px;
    margin: 1px auto 10px;
  }

  .login_border {
    background-color: rgba(255, 255, 255, 0.4);
    padding: 30px 30px 10vh;
    border-radius: 10px;
    box-shadow: 0px 0px 15px 5px rgba(0, 0, 0, 0.14);
  }

  @media (max-height: 400px) {
    .login_box {
      // top: 2px;
      // transform: translate(-50%, 0%);
    }
  }

  .logo_wrap {
    width: 100%;

    .logo {
      width: 250px;
      margin: calc(10vh - 28px) auto;
      text-align: center;

      img {
        width: 100%;
      }
    }
  }

  label {
    font-size: 15px;
    color: #414141;
  }

  .submit_btn {
    margin: 20px 0;
  }

  .warn_wrap {
    position: absolute;
    width: 100vw;
    margin: 10px auto;
    text-align: center;
    font-family: 'Nanum Gothic', 'sans-serif';
    font-size: 15px;
    left: 50%;
    transform: translateX(-50%);

    .warn_content {
      max-width: 630px;
      margin: 0 auto 40px;
      text-align: left;

      ol {
        font-weight: bold;
        color: #616161;
        padding: 10px;
        word-break: keep-all;

        li {
          color: #d22323;
          padding: 5px 0;
          text-align: center;
        }
      }
    }
  }

  .copy_right {
    width: 100%;
    text-align: center;
    font-weight: bold;
    font-size: 15px;
    color: #515151;
  }

  .form-control, .btn-info {
    box-shadow: 0px 0px 10px 1px rgba(0, 0, 0, 0.14);
  }
</style>
