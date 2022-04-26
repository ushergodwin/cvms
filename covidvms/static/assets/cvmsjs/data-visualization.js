jQuery(() => {
    plotGraph(
        {
            url: $("#partial_chart").data('url'), 
            id: 'partial_chart',
            label: 'Population that received the 1st Doze Per District',
            params: {
                min: $("#partial_chart").data('min'),
                max: $("#partial_chart").data('max')
            }
    });
    let min_val = 1;
    let max_val = 1;
    $("#p_show_more").on('click', function(){
        min_val += 30;
        max_val += 30 * 2;
        if(max_val > $(this).data('dist_no'))
        {
            min_val = 1;
            max_val = 30
        }
        $("#p_min_val").html(min_val);
        $("#p_of").html("to");
        $("#p_max_val").html(max_val);
        plotGraph(
            {
                url: $("#partial_chart").data('url'), 
                id: 'partial_chart',
                label: 'Population that received the 1st Doze Per District',
                params: {
                    min: min_val,
                    max: max_val
                }
        }); 
    });
    $("#f_show_more").on('click', function(){
        min_val += 30;
        max_val += 30 * 2;
        if(max_val > $(this).data('dist_no'))
        {
            min_val = 1;
            max_val = 30
        }
        $("#f_min_val").html(min_val);
        $("#f_of").html("to");
        $("#f_max_val").html(max_val);
        plotGraph2(
            {
                url: $("#fully_vaccinated_chart").data('url'), 
                id: 'fully_vaccinated_chart',
                label: 'Population that received the 2st Doze Per District',
                params: {
                    min: min_val,
                    max: max_val
                }
        }); 
    })
});

function plotGraph(setting = {})
{
    $.ajax({
        url: window.location.origin + setting.url,
        type: 'GET',
        data: setting.params,
        beforeSend: ()=> {
            $(".partial_chart").html("<span class='spinner-border spinner-border-sm text-primary'></span> Loading chart...")
        },
        success: function (data)
        {
            $(".partial_chart").html("");
            var districts = [];
            var vaccination = [];
            //console.log(data.length)
             for (let index = 0; index < data.length; index++) {
                 districts.push(data[index].district)
                 vaccination.push(data[index].vaccination)
             }
            //  console.log(vaccination);

            var chartdata = {
                labels: districts,
                datasets: [
                    {
                        label: setting.label,
                        backgroundColor: '#49e2ff',
                        borderColor: '#46d5f1',
                        hoverBackgroundColor: '#800080',
                        hoverBorderColor: '#666666',
                        data: vaccination
                    }
                ]
            };

            var graphTarget = $("#"+setting.id);
            plotGraph2(
                {
                    url: $("#fully_vaccinated_chart").data('url'), 
                    id: 'fully_vaccinated_chart',
                    label: 'Population that received the 2st Doze Per District',
                    params: {
                        min: $("#fully_vaccinated_chart").data('min'),
                        max: $("#fully_vaccinated_chart").data('max')
                    }
            });
            return new Chart(graphTarget, {
                type: 'bar',
                data: chartdata
            });
        }
    });
}

function plotGraph2(setting = {})
{
    $.ajax({
        url: window.location.origin + setting.url,
        type: 'GET',
        data: setting.params,
        beforeSend: ()=> {
            $(".partial_chart").html("<span class='spinner-border spinner-border-sm text-primary'></span> Loading chart...")
        },
        success: function (data)
        {
            $(".partial_chart").html("");
            var districts = [];
            var vaccination = [];
            //console.log(data.length)
             for (let index = 0; index < data.length; index++) {
                 districts.push(data[index].district)
                 vaccination.push(data[index].vaccination)
             }
            //  console.log(vaccination);

            var chartdata = {
                labels: districts,
                datasets: [
                    {
                        label: setting.label,
                        backgroundColor: '#49e2ff',
                        borderColor: '#46d5f1',
                        hoverBackgroundColor: '#800080',
                        hoverBorderColor: '#666666',
                        data: vaccination
                    }
                ]
            };

            var graphTarget = $("#"+setting.id);

            return new Chart(graphTarget, {
                type: 'bar',
                data: chartdata
            });
        }
    });
}