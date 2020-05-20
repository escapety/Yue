<template>
  <el-form :model="user" :rules="rules" ref="newuser">
    <el-form-item label="用户名" prop="name">
      <el-input v-model="user.name" clearable></el-input>
    </el-form-item>
    <el-form-item label="密码" prop="password">
      <el-input v-model="user.password" show-password clearable></el-input>
    </el-form-item>
    <el-form-item label="确认密码" prop="checkpassword">
      <el-input v-model="user.checkpassword" show-password clearable></el-input>
    </el-form-item>
    <el-alert title="注册失败" type="error" center :closable="false" v-show="showerror"></el-alert>
    <el-form-item>
      <el-button type="primary" @click="register">注册</el-button>
    </el-form-item>
  </el-form>
</template>
<script>
export default {
  data () {
    var checkPassword = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请重复密码'))
      } else if (value !== this.user.password) {
        callback(new Error('两次输入密码不一致'))
      } else {
        callback()
      }
    }
    return {
      user: {
        name: '',
        password: '',
        checkpassword: ''
      },
      showerror: false,
      rules: {
        name: [
          { required: true, message: '请输入用户名', triggle: 'blur' },
          { min: 5, message: '长度至少为5个字符', triggle: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', triggle: 'blur' }
        ],
        checkpassword: [
          { required: true, validator: checkPassword, triggle: 'blur' }
        ]
      }
    }
  },
  methods: {
    register () {
      let _this = this
      this.$refs['newuser'].validate((valid) => {
        if (valid) {
          this.$axios({
            method: 'get',
            url: '/BackEnd/new_user/',
            params: {
              name: _this.user.name,
              password: _this.user.password
            }
          })
            .then(function (response) {
              console.log(response.data)
              // if (response.data === 'OK') {
              //   _this.$router.push('main')
              // } else {
              //   _this.showerror = true
              // }
              _this.$cookies.set('userid', response.data.user_id)
              _this.$router.push('main')
            })
            .catch(function (error) {
              _this.showerror = true
              console.log(error)
            })
        }
        this.$refs['newuser'].resetFields()
      })
    }
  }
}
</script>
