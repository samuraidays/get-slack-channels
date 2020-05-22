import os
import slack 
import json
import pandas as pd 


# チャンネルの取得
def get_channels(client):
    channels = client.conversations_list(limit=1000)
    if channels['ok']:
        return channels['channels']
    else:
        assert channels['ok']
        return None


if __name__ == '__main__':
    cli = slack.WebClient(token=os.environ['SLACK_API_TOKEN'])
    channels = get_channels(cli)

    json_data = json.dumps(channels)
    with open("channel_list.json", 'w') as fp:
        json.dump(channels, fp)

    df = pd.DataFrame(channels, columns=channels[0].keys())

    df.to_csv("channel_list.csv")
