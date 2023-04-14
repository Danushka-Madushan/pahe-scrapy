const search = document.getElementById('search')
const namebox = document.getElementById('name')

search.onclick = async () => {
    const response = await axios.get(`/api/search/${namebox.value}`)
    document.getElementById('content').innerText = JSON.stringify(response.data, null, 4)
}
