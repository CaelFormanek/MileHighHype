import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [articles, setArticles] = useState([]);

  // Define a list of colors for the headlines
  const colors = ["#FB4F14", "#87CEEB", "#6F263D", "#33006F"]; // Orange, Light Blue, Avalanche Red, Purple

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/news/')
      .then(response => setArticles(response.data))
      .catch(error => console.error("Error fetching data:", error));
  }, []);

  return (
    <div className="App">
      <h1 style={{ textAlign: 'center', marginBottom: '20px' }}>Sports News</h1>
      <div
        style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
          gap: '20px',
          padding: '20px',
        }}
      >
        {articles.map((article, index) => (
          <div
            key={index}
            style={{
              border: '1px solid #ddd',
              borderRadius: '8px',
              padding: '16px',
              boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
              backgroundColor: '#f9f9f9',
            }}
          >
            {/* Dynamic headline color */}
            <h2 style={{ color: colors[index % colors.length], marginBottom: '8px' }}>
              {article.title}
            </h2>
            {/* Display Date */}
            <p style={{ fontStyle: 'italic', color: '#555', marginBottom: '4px' }}>
              {article.date}
            </p>
            {/* Display Team */}
            <p style={{ fontWeight: 'bold', color: '#333', marginBottom: '12px' }}>
              Team: {article.team}
            </p>
            {/* Article Content */}
            <p style={{ lineHeight: '1.5', color: '#666' }}>{article.content}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
