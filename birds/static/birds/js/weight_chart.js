const ctx = document.getElementById('weightChart');

// Djangoから受け取った全データを保存
const allLabels = [...labels];
const allWeightData = [...weightData];

function parseDate(dateString) {
    const [year, month, day] = dateString.split('-').map(Number);
    return new Date(year, month - 1, day);
}

function filterData(days) {

    // 全期間
    if (days === 'all') {
        return {
            labels: allLabels,
            data: allWeightData
        };
    }

    const today = new Date();
    today.setHours(0, 0, 0, 0);

    const startDate = new Date(today);
    startDate.setDate(today.getDate() - Number(days));

    const filteredLabels = [];
    const filteredData = [];

    allLabels.forEach((label, index) => {

        const recordDate = parseDate(label);

        if (recordDate >= startDate && recordDate <= today) {
            filteredLabels.push(label);
            filteredData.push(allWeightData[index]);
        }
    });

    return {
        labels: filteredLabels,
        data: filteredData
    };
}


// 最初は1か月表示
const initialData = filterData(30);

const weightChart = new Chart(ctx, {
    type: 'line',

    data: {
        labels: initialData.labels,

        datasets: [{
            label: '体重(g)',
            data: initialData.data,
            tension: 0.2
        }]
    },

    options: {
        responsive: true,
        maintainAspectRatio: false,

        scales: {
            y: {
                beginAtZero: false
            }
        }
    }
});


// 期間切り替え
document.querySelectorAll('.period-btn').forEach(button => {

    button.addEventListener('click', function () {

        const days = this.dataset.days;

        const filtered = filterData(days);

        weightChart.data.labels = filtered.labels;
        weightChart.data.datasets[0].data = filtered.data;

        weightChart.update();

        // 選択中ボタンの見た目を変更
        document.querySelectorAll('.period-btn').forEach(btn => {
            btn.classList.remove('active');
        });

        this.classList.add('active');
    });

});