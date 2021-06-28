//importing the data using json
function buildCharts(sample) {
  d3.json("static/samples.json").then((data)=> {
    //console.log(data);
    var samples = data.samples;
    //console.log(samples);
    var resultsarray= samples.filter(sampleobject => 
      sampleobject.id == sample);
    var result= resultsarray[0]

    var ids = result.otu_ids;
    
    var labels = result.otu_labels;
    var values = result.sample_values;


    //bar
    var bar_data =[
      {
        y:ids.slice(0, 10).map(otuID => `OTU ${otuID}`).reverse(),
        x:values.slice(0,10).reverse(),
        text:labels.slice(0,10).reverse(),
        type:"bar",
        orientation:"h"
  
      }
    ];
  
    var barLayout = {
      title: "Top 10 Bacteria Cultures Found",
      margin: { t: 30, l: 150 }
    };
  
    Plotly.newPlot("bar", bar_data, barLayout);

    //bubble
    
    
    var LayoutBubble = {
      margin: { t: 0 },
      xaxis: { title: "OTU ID" },
      hovermode: "closest",
      };
  
      var DataBubble = [ 
      {
        x: ids,
        y: values,
        text: labels,
        mode: "markers",
        marker: {
          color: ids,
          size: values,
          }
      }
    ];
  
    Plotly.newPlot("bubble", DataBubble, LayoutBubble);




    

  });
}

//buildCharts();

function buildMetadata(sample) {
  d3.json("static/samples.json").then((data) => {
    //console.log(data);
    
    
    var metadata= data.metadata;

    //console.log(metadata);
    var resultsarray= metadata.filter(sampleobject => 
      sampleobject.id == sample);
    var result= resultsarray[0]
    
    var panel = d3.select("#sample-metadata");
    panel.html("");
    Object.entries(result).forEach(([key, value]) => {
      panel.append("h6").text(`${key}: ${value}`);
    });

  });
}
//buildMetadata();

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");
  
  // Use the list of sample names to populate the select options
  d3.json("static/samples.json").then((data) => {
    var sampleNames = data.names;
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });
  
    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
  }
  
  function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
  }
  
  
  
  // Initialize the dashboard
  init();


