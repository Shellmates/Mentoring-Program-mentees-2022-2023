const http = require('http');

const PORT = process.env.PORT || 5000;

// Create server object

http.createServer((req, res) => {
    // Write a response
    res.writeHead(200, {
        "Flag": "shellmates{1t_$t1ll_n33ds_t0_b3_s3nt_1n_th3_b0dy_th0}"
    })
    res.write('<h1>Welcome to My Special App</h1>');
    res.write("<p>I'm obviously the message sent to you, but what if...</p>");
    res.end();
}).listen(PORT, () => console.log(`Server running on port ${PORT} ...`))