
var auto_refresh_interval = undefined;
var auto_refresh = $('[data-refresh="auto"]');
startAutoRefreshInterval();

function startAutoRefreshInterval()
{
    console.log(auto_refresh.length)
  if (auto_refresh.length >= 0)
  {
    console.log('starting auto refresh interval');
    auto_refresh_interval = window.setInterval(function(){
      console.log('refreshing data');
      $.ajax({
        url: 'http://asfd',
        success: function( data ) {
          for (var i=auto_refresh.length-1; i>=0; i--)
          {
            var id = '#' + auto_refresh[i].id;
            console.log(id);
            $(id).html($(data).find(id).html());
          }
        }
      });
    }, 1000);
  }
}
