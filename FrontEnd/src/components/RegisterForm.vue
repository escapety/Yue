<template>
  <el-form :model="user" :rules="rules" ref="user">
    <el-form-item label="用户名" prop="name">
      <el-input v-model="user.name" clearable></el-input>
    </el-form-item>
    <el-form-item label="密码" prop="password">
      <el-input v-model="user.password" show-password clearable></el-input>
    </el-form-item>
    <el-form-item label="确认密码" prop="checkpassword">
      <el-input v-model="user.checkpassword" show-password clearable></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="register('user')">注册</el-button>
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
      rules: {
        name: [
          { required: true, message: '请输入用户名', triggle: 'blur' },
          { min: 5, message: '长度至少为5个字符', triggle: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', triggle: 'blur' }
        ],
        checkpassword: [
          { validator: checkPassword, triggle: 'blur' }
        ]
      }
    }
  },
  methods: {
    register (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.$axios({
            method: 'get',
            url: '/BackEnd/new_user/',
            param: {
              name: this.name,
              password: this.password
            }
          })
            .then(function (response) {
              console.log(response)
            })
        } else {
          this.$refs[formName].resetFields()
        }
      })
    }
  }
}
</script>
