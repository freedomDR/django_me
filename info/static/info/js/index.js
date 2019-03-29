var myMusic = new Vue({
                      el:'#my_music',
                      data:{
                          name: 'vue.js'
                      },
                      methods:{
                          myalert: function(event){
                              console.log('hello'+this.name+'!')
                              alert('hello '+this.name+'!')
                          },
                          go: function(message){
                              alert('即将转向'+message)
                          }
                      }

})
