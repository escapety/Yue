<template>
  <el-form :model="user" :rules="rules" ref="user">
    <el-form-item label="用户名" prop="name">
      <el-input v-model="user.name" clearable></el-input>
    </el-form-item>
    <el-form-item label="密码" prop="password">
      <el-input v-model="user.password" type="password" clearable></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="login('user')">登录</el-button>
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
    login (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.$router.push('main')
          // axios({
          //   method: 'get',
          //   url: '/BackEnd/authentication',
          //   params: {
          //     name: 'myuser',
          //     password: 'abcde'
          //   }
          // })
          //   .then(function (response) {
          //     console.log(response)
          //   })
          //   .catch(function (error) {
          //     console.log(error)
          //   })
        } else {
          this.$refs[formName].resetFields()
        }
      })
    }
  }
}
</script>
