/**
 * @param {number[]} startTime
 * @param {number[]} endTime
 * @param {number} queryTime
 * @return {number}
 */
var busyStudent = function (startTime, endTime, queryTime) {
    let res = 0;
    for (let i = 0; i < startTime.length; i++) {
        let star = startTime[i];
        let end = endTime[i];
        if (star <= queryTime && end >= queryTime) {
            res++;
        }
    }
    return res;
};