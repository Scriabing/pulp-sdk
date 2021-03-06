/*
 * Copyright (C) 2020 GreenWaves Technologies, SAS, ETH Zurich and
 *                    University of Bologna
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/* 
 * Authors: Germain Haugou, GreenWaves Technologies (germain.haugou@greenwaves-technologies.com)
 */


#include <vp/vp.hpp>



class cluster : public vp::component
{

public:

  cluster(js::config *config);

  int build();
  void start();

private:

  vp::power_trace power_trace;

};

cluster::cluster(js::config *config)
: vp::component(config)
{

}


int cluster::build()
{
  if (this->power.new_trace("power_trace", &this->power_trace)) return -1;

  return 0;
}


void cluster::start()
{
  this->power_trace.collect();
}



extern "C" vp::component *vp_constructor(js::config *config)
{
  return new cluster(config);
}
