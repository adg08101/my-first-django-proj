window.addEventListener('load', function () {
    let app = new Vue({
          el: '#app',
          delimiters: ['[[', ']]'],
          data: {
            id: null,
            group: true,
          },
          methods: {
                even: function(val, mode = null) {
                    if(mode) {
                        if(mode == 'group') {
                            if(this.id == null) {
                                this.id = val
                                this.group = !this.group
                            } else {
                                if(this.id != val) {
                                    this.id = val
                                    this.group = !this.group
                                }
                            }
                            return this.group
                        }
                    }
                    return val % 2
                },
                back: function() {
                    window.history.back();
                },
                goto: function(url) {
                    window.location = url;
                },
          }
    })
    if(document.getElementById('choices')){
        let obj = new vanillaSelectBox("#choices", {
        "search": true,
        })
    }
})
