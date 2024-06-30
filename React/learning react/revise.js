function destructuring() {
    const cars = [
        {
          model: "Honda Civic",
          //The top colour refers to the first item in the array below:
          //i.e. hondaTopColour = "black"
          coloursByPopularity: ["black", "silver"],
          speedStats: {
            topSpeed: 140,
            zeroToSixty: 8.5,
          },
        },
        {
          model: "Tesla Model 3",
          coloursByPopularity: ["red", "white"],
          speedStats: {
            topSpeed: 150,
            zeroToSixty: 3.2,
          },
        },
      ];

      const [honda, tesla] = cars;
      const {
        coloursByPopularity: [teslaTopColour],
        speedStats: { topSpeed: teslaTopSpeed },
      } = tesla;
      const {
        coloursByPopularity: [hondaTopColour],
        speedStats: { topSpeed: hondaTopSpeed },
      } = honda;

      console.log(tesla.model,teslaTopSpeed,teslaTopColour)     // Task is to log these 2 lines without changing them
      console.log(honda.model,hondaTopSpeed,hondaTopColour)
}

destructuring()