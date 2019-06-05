genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays = [500, 600, 150, 800, 2500]

a,b,c=list(enumerate(zip(genres,plays)))[0]

def solution(genres, plays):
    answer = []
    id_cate = {}
    id_play_nums = {}
    cate_play_nums = {}
    for id,info in enumerate(zip(genres,plays)):
        id_play_nums[id] = info[1]

        try:
            id_cate[info[0]].append(id)
        except:
            id_cate[info[0]] = [id]

        try:
            cate_play_nums[info[0]] +=info[1]
        except KeyError:
            cate_play_nums[info[0]] = info[1]

    for cate in sorted(cate_play_nums,key=lambda x:cate_play_nums[x],reverse=True):
        for id in sorted(id_cate[cate],key=lambda x:id_play_nums[x],reverse=True)[:2]:
            answer.append(id)
    return answer
