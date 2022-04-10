import React from 'react';
import Restaurant from './Restaurant';
const Restaurants = ({ restaurants, removeRestaurant }) => {
  return (
    <section>
      <div className="title">
        {restaurants.length > 0 && <h3>Suggested Restaurants</h3>}
        {restaurants.length > 0 && <div className="underline"></div>}
      </div>
      <div>
        {restaurants.map((restaurant) => {
          return <Restaurant key={restaurant.business_id} {...restaurant} removeRestaurant={removeRestaurant} />;
        })}
      </div>
    </section>
  );
};

export default Restaurants;