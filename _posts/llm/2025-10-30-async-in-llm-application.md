---
layout: post
title: LLM 애플리케이션에서 비동기 처리의 중요성
image:
  path: https://images.unsplash.com/photo-1591267990532-e5bdb1b0ceb8?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=2627
description: >
  
categories: llm
sitemap:
  changefreq: weekly
comments: true
---

<!-- START RADAR CHART EMBED -->
<div style="width: 100%; max-width: 600px; margin: 2rem auto; font-family: sans-serif;">
    <h3 style="text-align: center; color: #333; margin-bottom: 1rem;">LangGraph vs. Google ADK</h3>
    <div style="position: relative; height: 400px; width: 100%;">
        <canvas id="frameworkRadarChart"></canvas>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
        (function() {
            const ctx = document.getElementById('frameworkRadarChart');
            if (!ctx) return;
            new Chart(ctx, {
                type: 'radar',
                data: {
                    labels: [
                        'Control Flow Flexibility',
                        'Deployment Ease',
                        'Enterprise Security',
                        'Ecosystem Support',
                        'State Transparency',
                        'Visual Prototyping'
                    ],
                    datasets: [
                        {
                            label: 'LangGraph',
                            data: [5, 2, 2, 5, 5, 3],
                            fill: true,
                            backgroundColor: 'rgba(59, 130, 246, 0.2)', // Blue
                            borderColor: 'rgb(59, 130, 246)',
                            pointBackgroundColor: 'rgb(59, 130, 246)',
                            pointBorderColor: '#fff',
                            pointHoverBackgroundColor: '#fff',
                            pointHoverBorderColor: 'rgb(59, 130, 246)'
                        },
                        {
                            label: 'Google ADK',
                            data: [2, 5, 5, 3, 3, 5],
                            fill: true,
                            backgroundColor: 'rgba(22, 163, 74, 0.2)', // Green
                            borderColor: 'rgb(22, 163, 74)',
                            pointBackgroundColor: 'rgb(22, 163, 74)',
                            pointBorderColor: '#fff',
                            pointHoverBackgroundColor: '#fff',
                            pointHoverBorderColor: 'rgb(22, 163, 74)'
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            position: 'bottom',
                        }
                    },
                    scales: {
                        r: {
                            beginAtZero: true,
                            max: 5,
                            min: 0,
                            ticks: {
                                stepSize: 1,
                                display: false // Hides the numbers on the rings for a cleaner look
                            },
                            grid: {
                                color: '#e5e5e5'
                            },
                            pointLabels: {
                                font: {
                                    size: 12
                                },
                                color: '#666'
                            }
                        }
                    }
                }
            });
        })();
    </script>
</div>
<!-- END RADAR CHART EMBED -->