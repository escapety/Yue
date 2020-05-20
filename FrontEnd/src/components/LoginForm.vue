<template>
  <el-form :model="user" :rules="rules" ref="user">
    <el-form-item label="用户名" prop="name">
      <el-input v-model="user.name" clearable></el-input>
    </el-form-item>
    <el-form-item label="密码" prop="password">
      <el-input v-model="user.password" type="password" clearable></el-input>
    </el-form-item>
    <el-alert title="登录失败" type="error" center :closable="false" v-show="showerror"></el-alert>
    <el-form-item>
      <el-button type="primary" @click="login">登录</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
export default {
  data () {
    return {
      user: {
        name: '',
        password: ''
      },
      showerror: false,
      rules: {
        name: [
          { required: true, message: '请输入用户名', triggle: 'blur' },
          { min: 5, message: '长度至少为5个字符', triggle: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', triggle: 'blur' }
        ]
      }
    }
  },
  methods: {
    login () {
      let _this = this
      this.$refs['user'].validate((valid) => {
        if (valid) {
          this.$axios({
            method: 'get',
            url: '/BackEnd/authentication/',
            params: {
              name: _this.user.name,
              password: _this.user.password
            }
          })
            .then(function (response) {
              console.log(response.data)
              if (response.data === 'OK') {
                _this.$router.push('main')
              } else {
                _this.showerror = true
              }
            })
            .catch(function (error) {
              _this.showerror = true
              console.log(error)
            })
        }
        this.$refs['user'].resetFields()
      })
    }
  }
}
</script>
